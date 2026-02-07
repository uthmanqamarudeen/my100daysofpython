from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("green")
        self.penup()
        self.refresh()


    def refresh(self):
        food_xcor = random.randint(-280, 270)
        food_ycor = random.randint(-280, 270)
        self.goto(food_xcor, food_ycor)