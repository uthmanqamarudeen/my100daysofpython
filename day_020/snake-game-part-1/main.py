from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game!")
screen.bgcolor("black")
screen.tracer(0)

# snake_segments = []
# x_pos = 0
# for i in range(3):
#     new_snake_segment = Turtle("square")
#     new_snake_segment.color("white")
#     new_snake_segment.penup()
#     new_snake_segment.goto(x=x_pos, y=0)
#     x_pos -= 20
#     snake_segments.append(new_snake_segment)
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.2)
    snake.move()








screen.exitonclick()
