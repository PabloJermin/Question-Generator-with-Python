from turtle import Turtle, Screen

tandy = Turtle()

def m_forward():
    tandy.forward(10)

def b_back():
    tandy.back(10)

def l_turn():
    tandy.left(10)

def r_turn():
    tandy.right(10)

def home():
    tandy.penup()
    tandy.clear()
    tandy.home()
    tandy.pendown() 


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=m_forward)
screen.onkey(key="s", fun=b_back)
screen.onkey(key="d", fun=l_turn)
screen.onkey(key="h", fun=home)
screen.onkey(key="r", fun=r_turn)
screen.exitonclick()