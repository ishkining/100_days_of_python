import turtle
import random

import colorgram


rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    new_color = color.rgb
    rgb_colors.append((int(new_color.r), int(new_color.g), int(new_color.b)))

timmy = turtle.Turtle()
timmy.speed("fastest")
turtle.colormode(255)
timmy.penup()
timmy.sety(-300)
timmy.setx(-300)

for line in range(10):
    for pace in range(10):
        timmy.color(random.choice(rgb_colors))
        timmy.begin_fill()
        timmy.circle(20)
        timmy.end_fill()
        timmy.forward(50)
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)


screen = turtle.Screen()
screen.exitonclick()