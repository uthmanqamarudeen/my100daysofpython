from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # On collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_after_wall()

    # On collision with paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_after_paddle()
        time.sleep(0.01)

    # When the right paddle misses
    if ball.xcor() > 380:
        ball.move_towards_left()
        scoreboard.l_point()

    # When the left paddle misses
    if ball.xcor() < -380:
        ball.move_towards_right()
        scoreboard.r_point()


screen.exitonclick()