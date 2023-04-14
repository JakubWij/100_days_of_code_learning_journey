from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-280, 250)
        self.current_level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f" Level: {self.current_level}", align="left", font=FONT)

    def game_over_sign(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

    def adding_level(self):
        self.current_level += 1
