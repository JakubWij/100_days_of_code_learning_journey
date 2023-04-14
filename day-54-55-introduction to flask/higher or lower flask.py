from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(0, 9)

@app.route("/")
def home_page():
    return "<h1><b>Guess a number between 0 and 9</b></h1>" \
           "<p><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></p>"

@app.route("/<int:number>")
def guess(number):
    if number == random_number:
        return "<h1>You found me!</h1>" \
               "<p><img src='https://media.giphy.com/media/8P1oO2JbrZK2uSYnL6/giphy.gif'></p>"
    elif number > random_number:
        return "<h1>Too high, try again!</h1>" \
               "<p><img src='https://media.giphy.com/media/wHB67Zkr63UP7RWJsj/giphy.gif'></p>"
    elif number < random_number:
        return "<h1>Too low, try again!</h1>" \
               "<p><img src='https://media.giphy.com/media/2uI9astifwiSUWVOTT/giphy.gif'></p>"


if __name__ == "__main__":
    app.run(debug=True)
