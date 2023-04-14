import turtle
from turtle import Turtle, Screen
import random


def random_color():
    return tim.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))



turtle.colormode(255)
tim = Turtle()
tim.speed(0)
tim.shape("turtle")
tim.color("chartreuse")
tim.hideturtle()




# pen up pen down means turtle will write a line or not
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# # TODO.1 draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
# random color, side is 100 len


# angle = 360
# counter = 2
# for _ in range(8):
#     counter += 1
#     random_color()
#     for _ in range(counter):
#         tim.forward(100)
#         tim.right(angle/counter)


# TODO.2 random walk + thickness + higher speed
# tim.width(10)
# directions = [0, 90, 180, 270]
#
# for _ in range(500):
#     random_color()
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# TODO 3 spirograph, make number of circles each with radious of 100 distance
size_of_gap = 5

for _ in range(int(360 / size_of_gap)):
    random_color()
    tim.circle(100)
    tim.setheading(tim.heading() + size_of_gap)




# turtle.getcanvas().postscript(file="duck.eps")
screen = Screen()
screen.exitonclick()
