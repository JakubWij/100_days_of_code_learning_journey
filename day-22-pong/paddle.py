from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.coordinates = coordinates
        self.penup()
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(self.coordinates)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)

