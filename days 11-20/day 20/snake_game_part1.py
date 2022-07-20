from turtle import Turtle, Screen
import time

from snake import Snake


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# TODO: 1: Create a snake body

snake = Snake()

# TODO: 3: Control the snake

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# TODO: 2: Move the snake
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
screen.exitonclick()