from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:number>')
def post(number):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    chosen_post = Post(all_posts, number - 1)
    print(all_posts)
    print(chosen_post.id)
    return render_template("post.html", title=chosen_post.title, subtitle=chosen_post.subtitle, body=chosen_post.body, number=chosen_post.id)

if __name__ == "__main__":
    app.run(debug=True)
