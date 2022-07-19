from turtle import Turtle, Screen
import random
timmy = Turtle()

for shape in range(3, 10):
    for side in range(shape):
        timmy.right(360/shape)
        timmy.forward(100)
    timmy.color([random.random(), random.random(), random.random()])


screen = Screen()
screen.exitonclick()
