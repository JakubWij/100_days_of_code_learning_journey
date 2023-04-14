from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


with app.app_context():
    db.create_all()




@app.route('/')
def home():
    with app.app_context():
        all_books = db.session.query(Book).all()
    return render_template("index.html", books_list=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        with app.app_context():
            new_book = Book(title=request.form["book_name"],
                            author=request.form["book_author"],
                            rating=request.form["book_rating"])
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("add.html")

@app.route("/edit", methods=["POST", "GET"])
def edit():
    if request.method == "POST":
        while app.app_context():
            book_id = request.form["id"] # from form get id by request
            book_to_update = Book.query.get(book_id) # by id chose book
            book_to_update.rating = request.form["rating"] # assign new value to chosen book rating
            db.session.commit()
            return redirect(url_for("home"))
    # part for showing book data (get method)
    # that's the hard part so from index.html in url_for we pass book.id as an id value.
    # id value is passed through URL so /edit?id=1 and args. get takes it
    book_id = request.args.get("id")
    book_selected = Book.query.get(book_id)
    return render_template("edit_rating.html", book=book_selected)


if __name__ == "__main__":
    app.run(debug=True)
