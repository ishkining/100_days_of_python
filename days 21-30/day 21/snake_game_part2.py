from turtle import Turtle, Screen
import time

from snake import Snake
from food import Food
from score import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# TODO: 1: Create a snake body

snake = Snake()
food = Food()
score = Score()

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

    # TODO: 4: Detect collision with food
    if snake.snake_body[0].distance(food) < 15:
        snake.extend_segment()
        score.refresh_score()
        food.refresh()

    # TODO 5: Detect collision with wall
    if snake.snake_body[0].xcor() > 280 or snake.snake_body[0].xcor() < -280 \
            or snake.snake_body[0].ycor() > 280 or snake.snake_body[0].ycor() < -280:
        is_game_on = False
        score.game_over()

    for segment in snake.snake_body[1:]:
        if snake.snake_body[0].distance(segment) < 10:
            is_game_on = False
            score.game_over()


screen.exitonclick()