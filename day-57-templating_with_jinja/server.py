from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home_page():
    current_date = datetime.now().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, date=current_date, name="James")

@app.route("/guess/<path:name>")
def guess_page(name):
    agify_response = requests.get(f"https://api.agify.io?name={name}").json()
    guessers_age = agify_response["age"]
    genderize_response = requests.get(f"https://api.genderize.io?name={name}").json()
    guessers_gender = genderize_response["gender"]
    var2 = 2
    return render_template("index2.html", guessers_name=name, v1=guessers_gender, v2=guessers_age)

@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    print(all_posts)
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
