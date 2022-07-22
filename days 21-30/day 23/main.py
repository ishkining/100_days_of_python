import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# TODO: 1: Move the turtle with keypress

player = Player()

screen.listen()
screen.onkey(player.move_forward, "w")

# TODO: 2: Create and move the cars

car_manager = CarManager()

# TODO: 5: Create scoreboard

scoreboard = Scoreboard()

speed_increment = 1
game_is_on = True
while game_is_on:
    car_manager.create_mess()
    time.sleep(0.1)
    car_manager.move_cars(speed_increment)
    screen.update()

    # TODO: 3: Detect collision with car

    for car in car_manager.cars:
        if car.xcor() - 40 < player.xcor() < car.xcor() + 40 and abs(player.ycor() - car.ycor()) < 18:
            game_is_on = False

    # TODO: 4: Detect when turtle reaches the other side

    if player.is_turtle_reached():
        speed_increment += 1
        player.start_position()
        car_manager.new_level()
        scoreboard.update_score(speed_increment)

screen.exitonclick()
