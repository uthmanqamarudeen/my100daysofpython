import turtle
from turtle import Turtle, Screen
import random

my_turtle = Turtle()
# my_turtle.shape("turtle")
# my_turtle.color("green")
# for i in range(4):
#     my_turtle.forward(100)
#     my_turtle.right(90)


# for i in range(15):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()



# polygon = 3
# color = ["red", "green", "blue", "black", "midnight blue", "dark red", "yellow"]
# my_turtle.penup()
# my_turtle.goto(-50, 100)
# my_turtle.pendown()
# #
# # while polygon < 10:
# #     my_turtle.color(random.choice(color))
# #     angle_of_rotation = 360 / polygon
# #     for i in range(polygon):
# #         my_turtle.forward(100)
# #         my_turtle.right(angle_of_rotation)
# #     polygon += 1
#
turtle.colormode(255)
def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour
# #
# # change_direction = [0, 90, 180, 270]
# #
# # for i in range(400):
# #     my_turtle.speed("fastest")
# #     my_turtle.color(random_colour())
# #     my_turtle.pensize(10)
# #     my_turtle.forward(25)
# #     direction = random.choice(change_direction)
# #     my_turtle.setheading(direction)
total_angle = 0

while total_angle < 360:
    my_turtle.color(random_colour())
    my_turtle.speed("fastest")
    my_turtle.circle(100)
    if total_angle  % 7 == 0:
        angle_of_rotation = 10
        my_turtle.left(angle_of_rotation)
        total_angle += angle_of_rotation
    else:
        angle_of_rotation = 5
        my_turtle.left(angle_of_rotation)
        total_angle += angle_of_rotation

screen = Screen()
screen.exitonclick()








