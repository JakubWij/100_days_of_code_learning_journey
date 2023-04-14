from flask import Flask, render_template, request
import requests
import smtplib


app = Flask(__name__)
n_point_data = requests.get("https://api.npoint.io/e5eff71efae071833fd2").json()

print(n_point_data)

@app.route("/")
@app.route("/index.html")
def home_page():
    return render_template("index.html", posts=n_point_data)

@app.route("/about.html")
def about_page():
    return render_template("about.html")

@app.route("/contact.html", methods=["POST", "GET"])
def contact_page():
    if request.method == "GET":
        return render_template("contact.html", msg_sent=False)
    elif request.method == "POST":
        username = request.form["username"]
        email = request.form["user_email"]
        phone = request.form["user_phone"]
        message = request.form["user_message"]
        send_mail(username, email, phone, message)
        return render_template("contact.html", msg_sent=True)

@app.route('/post/<int:index>')
def post_page(index):
    requested_post = None
    for blog_post in n_point_data:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

def send_mail(name, email, phone, message):
    # connection and mail
    my_email = "jakubwijtest@gmail.com"
    password = "czir ukmc fnja mbvg"
    connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=120)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=email, to_addrs=my_email, msg=f"Subject:Blog's msg\n\nUsername:{name}"
                                                                f"\nEmail:{email}"
                                                                f"\nPhone: {phone},"
                                                                f"\nMessage: {message}")
    connection.close()

if __name__ == "__main__":
    app.run(debug=True)