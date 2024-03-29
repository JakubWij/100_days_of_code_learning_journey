from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.app_context().push()

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # # Method 1.
        # dictionary = {}
        # # Loop through each column in the data record
        # for column in self.__table__.columns:
        #     # Create a new dictionary entry;
        #     # where the key is the name of the column
        #     # and the value is the value of the column
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random")
def get_random():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    print(random_cafe)
    # cafe={"id": random_cafe.id,
    #                          "name": random_cafe.name,
    #                          "map_url": random_cafe.map_url,
    #                          "img_url": random_cafe.img_url,
    #                          "location": random_cafe.location,
    #                          "has_toilet": random_cafe.has_toilet,
    #                          "has_sockets": random_cafe.has_sockets,
    #                          "has_wifi": random_cafe.has_wifi,
    #                          "can_take_calls": random_cafe.can_take_calls,
    #                          "seats": random_cafe.seats,
    #                          "coffee_price": random_cafe.coffee_price
    #                          }
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def get_all():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafe=[cafe.to_dict() for cafe in cafes])

@app.route("/search")
def search_by_param():
    query_location = request.args.get("loc")
    cafes = db.session.query(Cafe).filter_by(location=query_location).all()
    if cafes:
        return jsonify(cafe=[cafe.to_dict() for cafe in cafes])
    else:
        return jsonify(error={"Not Found": "Sorry we dont have a cafe at that location."})


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    # request.form.get is from form and args is taking from ?new_value=...
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record put - shiping entire new bicycle so entire entry, patch- change one value like wheel
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    record_to_change = request.args.get("new_price")
    # cafe = db.session.query(Cafe).get(cafe_id)
    cafe = db.session.query(Cafe).filter_by(id=cafe_id).first()
    if cafe:
        cafe.coffee_price = record_to_change
        db.session.commit()
        return jsonify(success="Successfully updated the price"), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def cafe_closed(cafe_id):
    cafe = db.session.query(Cafe).get(cafe_id)
    api_key = "TopSecretAPIKey"
    query_api_key = request.args.get("api-key")
    if cafe:
        # cafe in db
        if api_key == query_api_key:
            # cafe in db correct key
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(success="Successfully deleted chosen cafe"), 200
        else:
            return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api_key"), 403
    else:
        # no cafe in db
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


if __name__ == '__main__':
    app.run(debug=True)
