from turtle import Turtle, Screen

tandy = Turtle()

def move_forward():
    tandy.forward(100)


screen = Screen()
screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()