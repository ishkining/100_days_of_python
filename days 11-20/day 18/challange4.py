from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.pensize(5)
for pace in range(100):
    if random.random() > 0.5:
        timmy.right(90)
    else:
        timmy.left(90)
    timmy.forward(30)
    timmy.color([random.random(), random.random(), random.random()])
    timmy.speed(6+0.03*pace)


screen = Screen()
screen.exitonclick()
