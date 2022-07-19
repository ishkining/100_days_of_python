from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.pensize(1)
timmy.speed("fastest")
timmy.circle(60)
for angle in range(0, 360, 10):
    timmy.color([random.random(), random.random(), random.random()])
    timmy.setheading(angle)
    timmy.circle(60)


screen = Screen()
screen.exitonclick()
