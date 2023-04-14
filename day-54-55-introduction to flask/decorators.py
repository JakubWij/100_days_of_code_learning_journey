"""http://www.cs.columbia.edu/~sedwards/classes/2015/1102-fall/Command%20Prompt%20Cheatsheet.pdf"""

from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function


# diffrent routes using app.route decorator
@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraf</p>' \
           '<img src="https://media.giphy.com/media/xT0BKCbFA2v8lEmTio/giphy.gif" width=300>'


# creating var paths and converting the path to a specified data type
@app.route("/bye")
@make_bold
@make_underlined
@make_emphasis
def say_bye():
    return "Bye!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"


if __name__ == "__main__":
    # run app in debig mode to auto-reload
    app.run(debug=True)
