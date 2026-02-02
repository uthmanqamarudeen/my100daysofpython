import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which will turtle will win the race? Enter a color: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = -125
turtle_lists = []

for i in range(6):
    my_turtle = Turtle(shape="turtle")
    my_turtle.color(colours[i])
    my_turtle.penup()
    my_turtle.goto(x = -230, y = y_pos)
    y_pos += 50
    turtle_lists.append(my_turtle)


is_race_on = True
while is_race_on:
    for turtle in turtle_lists:
        if turtle.xcor() > 210:
            is_race_on = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f"You win!. The {winner} turtle is the winner")
            else:
                print(f"You lose!. The {winner} turtle is the winner")


        turtle.forward(random.randint(0, 10))

screen.exitonclick()
