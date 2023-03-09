from turtle import Turtle, Screen


def move_forword():
    festus.forward(10)
def move_leftword():
    festus.left(10)
def move_rightword():
    festus.right(10)
def move_backword():
    festus.backward(10)
def clear():
    festus.home()
    festus.clear()


festus = Turtle()
screen = Screen()

screen.listen()
screen.onkey(fun=move_forword, key="Up")
screen.onkey(fun=move_leftword, key="Left")
screen.onkey(fun=move_rightword, key="Right")
screen.onkey(fun=move_backword, key="Down")
screen.onkey(fun=clear, key="c")
screen.exitonclick()