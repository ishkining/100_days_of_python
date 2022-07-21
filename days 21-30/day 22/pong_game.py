from turtle import Turtle, Screen
import time

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# TODO: 1: Create a Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong Game")
screen.tracer(0)

# TODO: 2: Create a Paddle and control it
player_paddle = Paddle(1)

screen.listen()
screen.onkey(player_paddle.move_up, "Up")
screen.onkey(player_paddle.move_down, "Down")

# TODO: 3: Create another Paddle
computer_paddle = Paddle(0)

# TODO: 4: Create a Ball
ball = Ball()

scoreboard = Scoreboard()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # TODO: 5: Bounce logic with wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.increment_y *= -1

    # TODO 6: Bounce ball with paddle
    if (ball.distance(player_paddle) < 50 and ball.xcor() > 320) \
            or (ball.distance(computer_paddle) < 50 and ball.xcor() < -320):
        ball.increment_x *= -1
        ball.move_speed *= 0.9

    # TODO 7: Detect if paddle misses ball
    if ball.xcor() > 380:
        ball.increment_x *= -1
        ball.goto(0, 0)
        scoreboard.point_to_computer()
        ball.move_speed = 0
    elif ball.xcor() < -380:
        ball.increment_x *= -1
        ball.goto(0, 0)
        scoreboard.point_to_player()
        ball.move_speed = 0

    computer_paddle.computer_move()

screen.exitonclick()