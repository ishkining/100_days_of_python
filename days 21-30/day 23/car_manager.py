from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []

    def create_mess(self):
        if random.randint(0, 4) > 3:
            self.create_car()

    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=3, stretch_len=1)
        new_car.up()
        new_car.speed("fastest")
        new_car.color(random.choice(COLORS))
        new_car.goto(280, random.randint(-250, 250))
        new_car.setheading(90)
        self.cars.append(new_car)

    def move_cars(self, increment):
        for car in self.cars:
            car.goto(car.xcor() - MOVE_INCREMENT * increment, car.ycor())

    def new_level(self):
        for car in self.cars:
            car.goto(700, 700)
        self.cars.clear()
