# import colorgram
#
# rgb = []
# colors = colorgram.extract("img.jpg", 30)
#
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     col = (r, g, b)
#     rgb.append(col)
#
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tandy = Turtle()
tandy.speed("fastest")
tandy.hideturtle()
list_of_col = [(35, 19, 15), (197, 144, 123), (30, 106, 155), (142, 85, 55), (9, 21, 45), (236, 213, 85),
               (196, 135, 155), (156, 62, 90), (221, 85, 66), (153, 17, 37), (202, 79, 104), (14, 54, 30),
               (162, 163, 35), (118, 172, 196), (41, 125, 79), (77, 12, 22), (120, 188, 160), (18, 92, 53),
               (11, 58, 137), (23, 201, 179), (23, 174, 206), (139, 222, 208), (149, 23, 16), (223, 172, 191),
               (233, 172, 162), (238, 206, 8)]

# setting the direction

tandy.setheading(220)
tandy.penup()
tandy.forward(400)
tandy.setheading(0)
tandy.penup()
number_of_dots = 100

# drawing the dots
for i in range(1, number_of_dots + 1):
    tandy.dot(20, random.choice(list_of_col))
    tandy.forward(50)
    tandy.dot(20, random.choice(list_of_col))

    # changing the directions for a new line
    if i % 10 == 0:
        tandy.setheading(90)
        tandy.forward(50)
        tandy.penup()
        tandy.left(90)
        tandy.forward(500)
        tandy.setheading(0)






screen = Screen()
screen.exitonclick
