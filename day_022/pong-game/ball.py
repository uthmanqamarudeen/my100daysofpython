from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(45)
        self.move_dir = self.heading()
        self.ball_speed = 0.1

    def move(self):
        self.forward(10)

    def bounce_after_wall(self):
        self.move_dir *= -1
        self.setheading(self.move_dir)

    def bounce_after_paddle(self):
        self.move_dir *= 3
        self.setheading(self.move_dir)
        self.ball_speed *= 0.9

    def move_towards_left(self):
        self.goto(0, 0)
        self.move_dir = 225
        self.setheading(self.move_dir)
        self.ball_speed = 0.1

    def move_towards_right(self):
        self.goto(0, 0)
        self.move_dir = 45
        self.setheading(self.move_dir)
        self.ball_speed = 0.1


