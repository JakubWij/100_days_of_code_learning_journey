from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

THE_MOVIE_DB_API_KEY = config['DEFAULT']['THE_MOVIE_DB_API_KEY']
API_ENDPOINT = "https://api.themoviedb.org/3/search/movie?"



app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


class RateMovieForm(FlaskForm):
    rating = StringField("Rating out of 10 eg. 7.5")
    review = StringField("Your review")
    submit = SubmitField('Done')


class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField('Add Movie')


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'
db.create_all()


## After adding the new_movie the code needs to be commented out/deleted.
## So you are not trying to add the same movie twice.
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()


@app.route("/")
def home():
    all_movies = db.session.query(Movie).order_by(Movie.rating).all()
    print(range(len(all_movies)))
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["POST", "GET"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie_selected = Movie.query.get(movie_id)
    if form.validate_on_submit():
        # movie_selected.rating = float(request.form["rating"])
        movie_selected.rating = float(form.rating.data)
        movie_selected.review = request.form["review"]
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie_selected, form=form)


@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_to_add = form.title.data
        params = {
            "api_key": THE_MOVIE_DB_API_KEY,
            "query": movie_to_add
        }
        response = requests.get(API_ENDPOINT, params=params)
        data = response.json()["results"]
        return render_template("select.html", form=form, data=data)
    return render_template("add.html", form=form)

@app.route("/find")
def find_movie():
    movie_id = request.args.get("id")
    if movie_id:
        find_id_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        response = requests.get(find_id_url, params={"api_key": THE_MOVIE_DB_API_KEY, "language": "en-US"})
        data = response.json()
        movie_title = data["original_title"]
        movie_img_url = f'https://image.tmdb.org/t/p/w300{data["poster_path"]}'
        movie_year = data["release_date"].split("-")[0]
        movie_description = data["overview"]
        new_movie = Movie(title=movie_title, year=movie_year, description=movie_description, img_url=movie_img_url)
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
