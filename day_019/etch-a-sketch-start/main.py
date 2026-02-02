from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()

def move_forwards():
    my_turtle.forward(10)

def move_backwards():
    my_turtle.backward(10)

def turn_clockwise():
    my_turtle.right(10)

def turn_anticlockwise():
    my_turtle.left(10)

def clear_screen():
    my_turtle.reset()


screen.listen()
screen.onkey(key="W", fun=move_forwards)
screen.onkey(key="S", fun=move_backwards)
screen.onkey(key="D", fun=turn_clockwise)
screen.onkey(key="A", fun=turn_anticlockwise)
screen.onkey(key="C", fun=clear_screen)
screen.exitonclick()
