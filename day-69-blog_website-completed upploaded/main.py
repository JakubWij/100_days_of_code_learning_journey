from flask import Flask, render_template, redirect, url_for, flash, request, abort
from functools import wraps
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
from flask_gravatar import Gravatar
from sqlalchemy import ForeignKey
import os
import smtplib

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
# app.config['SECRET_KEY'] = "..."
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
# Sqlite database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
# try PostgreSQL if not available then local db
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///blog.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# creating login manager and configure it for login
login_manager = LoginManager()
login_manager.init_app(app)


# creating admin decorator
def admin_only(function):
    # need wraps from functools
    @wraps(function)
    def wrapper_function(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return function(*args, **kwargs)

    return wrapper_function


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


##CONFIGURE TABLES


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    # this will act like a list of BlogPosts obj attached to each User
    # the author refers to the author property in the PlogPost class. its just making relationship not new column
    posts = relationship("BlogPost", back_populates="author")
    # parent relationship
    comments = relationship("Comment", back_populates="comment_author")


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    # create foreign key, "users.id" the users refers to the tablename of User
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # create reference to the User obj, the "posts" refers to the posts property in the User class
    # to acces author you need User obj.author.name by taping obj.author you get user obj and then .name gives property
    author = relationship("User", back_populates="posts")
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    # blogpost is parent for comment
    comments = relationship("Comment", back_populates="parent_post")


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    # child relationship
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")
    # child relationship to blokpost
    post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")


db.create_all()


def send_mail(name, email, phone, message):
    # connection and mail
    my_email = "jakubwijtest@gmail.com"
    password = "czir ukmc fnja mbvg"
    msg = f"Subject:Blog's msg\n\nUsername:{name}\nEmail:{email}\nPhone: {phone},\nMessage: {message}"
    connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=120)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=email, to_addrs=my_email, msg=msg.encode("utf-8"))
    connection.close()


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts, current_user=current_user)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        salt_hash_password = generate_password_hash(password=form.password.data,
                                                    method="pbkdf2:sha256",
                                                    salt_length=8)
        # if user's email allready exists in db
        if User.query.filter_by(email=form.email.data).first():
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for("login"))

        new_user = User(
            email=form.email.data,
            password=salt_hash_password,
            name=form.name.data
        )
        db.session.add(new_user)
        db.session.commit()
        # authenticate and login the user with flask-login
        login_user(new_user)
        return redirect(url_for("get_all_posts", current_user=current_user))
    return render_template("register.html", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if not user:
            flash("That email does not exist, please try again.")
            return redirect("login")
        elif not check_password_hash(user.password, password):
            flash("Incorrect password, please try again.")
            return redirect("login")
        else:
            login_user(user)
            return redirect(url_for("get_all_posts"))
    return render_template("login.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts', current_user=current_user))


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    comment_form = CommentForm()
    gravatar = Gravatar(app, size=100, rating="g", default="retro", force_default=False, force_lower=False,
                        use_ssl=False, base_url=None)
    if current_user.is_authenticated:
        if comment_form.validate_on_submit():
            new_comment = Comment(
                text=comment_form.comment_text.data,
                comment_author=current_user,
                parent_post=requested_post
            )
            db.session.add(new_comment)
            db.session.commit()
    else:
        flash("You need to log in or register to comment")
        return redirect(url_for("login"))
    return render_template("post.html", post=requested_post, current_user=current_user, comment_form=comment_form,
                           gravatar=gravatar)


@app.route("/about")
def about():
    return render_template("about.html", current_user=current_user)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", msg_sent=False)
    elif request.method == "POST":
        username = request.form["username"]
        email = request.form["user_email"]
        phone = request.form["user_phone"]
        message = request.form["user_message"]
        send_mail(username, email, phone, message)
        return render_template("contact.html", msg_sent=True, current_user=current_user)


@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,  # thats why it doesnt work
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, current_user=current_user)


@app.route("/edit-post/<int:post_id>")
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form, current_user=current_user)


@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(debug=True)
