#
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colour = (r,g, b)
#     rgb_colors.append(new_colour)
#
# print(rgb_colors)


import random
from turtle import Turtle, Screen
dot_turtle = Turtle()


colour_list = [(149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

dot_turtle.speed("fast")
dot_turtle.penup()
dot_turtle.hideturtle()
dot_turtle.setheading(225)
dot_turtle.forward(250)
dot_turtle.setheading(0)

total_dots = 101

for dot in range(1, total_dots):
    dot_turtle.dot(20, random.choice(colour_list))
    dot_turtle.forward(50)
    if dot % 10 == 0:
        dot_turtle.setheading(90)
        dot_turtle.forward(50)
        dot_turtle.setheading(180)
        dot_turtle.forward(500)
        dot_turtle.setheading(0)











screen = Screen()
screen.exitonclick()