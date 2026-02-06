from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="Left", font=FONT)

    def increase_score(self):
        self.level += 1
        self.update_score()

    def game_ends(self):
        self.penup()
        self.goto(0, 0)
        self.hideturtle()
        self.write("GAME OVER!", align="center", font=FONT)