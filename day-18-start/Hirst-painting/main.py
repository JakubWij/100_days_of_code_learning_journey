# import colorgram
#
#
# colors = colorgram.extract("image.jpg", 50)
#
#
#
# list_of_colors = []
# for color in colors:
#     list_of_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print(list_of_colors)
# TODO 10/10 painting 20 size and space between is 50
import random
import turtle
from turtle import Turtle, Screen

def random_color(tuple_color):
    tim.color(tuple_color)


color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83), (245, 205, 7), (35, 88, 88), (103, 24, 56)]


turtle.colormode(255)
tim = Turtle()
tim.speed(0)
tim.color("black")
tim.penup()
tim.hideturtle()
tim.setpos(-200, -200)
counter = 0
counter_2 = -200
while counter < 100:
    random_color(random.choice(color_list))
    tim.dot(20)
    tim.penup()
    tim.forward(50)
    counter += 1
    if counter % 10 == 0:
        counter_2 += 50
        tim.goto(-200, counter_2)













screen = Screen()
screen.exitonclick()
