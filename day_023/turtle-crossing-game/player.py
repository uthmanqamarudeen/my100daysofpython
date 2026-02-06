from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.finish_line = FINISH_LINE_Y

    def move_forward(self):
        self.forward(10)

    def move_backward(self):
        self.backward(10)

    def finish(self):
        self.reset()
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

