import random
import turtle
from turtle import Turtle, Screen
from random import Random

# drawing a square
tandy = Turtle()
tandy.shape("turtle")
tandy.color("blue")

# moving
# tandy.forward(100)
# tandy.right(90)
# tandy.forward(100)
# tandy.right(90)
# tandy.forward(100)
# tandy.right(90)
# tandy.forward(100)

# for i in range(4):
#     tandy.forward(100)
#     tandy.right(90)


# drawing dashed lines
# for i in range(15):
#     tandy.forward(10)
#     tandy.penup()
#     tandy.forward(10)
#     tandy.pendown()

#     drawing different shapes all in one

# c_list = ["CornFlowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat",
#           "SlateGray", "SeaGreen"]
# def draw_shape(sides):
#     deg = 360 / sides
#     for i in range(sides):
#         tandy.forward(100)
#         tandy.right(deg)
#
#
# for sides in range(3, 11):
#     draw_shape(sides)
# #     changing the color for each draw
#     tandy.color(random.choice(c_list))




# creating random colors
turtle.colormode(255)
def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup_color = (r, g, b)
    return tup_color

# creating random walks for the turtle
# directions = [0, 90, 180, 360]
# tandy.speed("fast")
#
# for i in range(1, 200):
#     tandy.color(random_colors())
#     tandy.pensize(5)
#     tandy.forward(20)
#     tandy.setheading(random.choice(directions))


# creating spirals

tandy.speed("fastest")

def drawing_circles(size):
    for i in range(int(360 / size)):
        tandy.pencolor(random_colors())
        tandy.circle(100)
        tandy.setheading(size + tandy.heading())

drawing_circles(5)
screen = Screen()
screen.exitonclick()
