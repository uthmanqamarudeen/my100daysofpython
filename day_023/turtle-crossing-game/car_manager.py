from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.move_increment = STARTING_MOVE_DISTANCE




    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car_y_pos = random.randint(-250, 250)
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(300, car_y_pos)
            self.cars.append(new_car)


    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_increment)

    def increase_speed(self):
        self.move_increment += MOVE_INCREMENT









