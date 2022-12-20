import turtle
from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title= 'Make your Choice', prompt='Which color will win? Red, Blue, Green or Yellow?')

# creating multiple instances with different states
y_position = [-22, 25, -45, 50, 0]
t_colors = ['red', 'blue', 'green', 'yellow', 'black']
t_list = []
for tit in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(t_colors[tit])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[tit])
    t_list.append(new_turtle)

if bet:
    race_on = True

# loop for race and checking winner
while race_on:
    for turt in t_list:
        if turt.xcor() > 230:
            race_on = False
            winner = turt.pencolor()
            if winner == bet:
                print("You win!")
            else:
                print(f"Sorry, you lost. {winner} color won!")
        random_dis = random.randint(0, 10)
        turt.forward(random_dis)




screen.exitonclick()