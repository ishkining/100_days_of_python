from turtle import Turtle, Screen

timmy = Turtle()

for pace in range(64):
    if pace % 2 == 0:
        timmy.up()
    else:
        timmy.down()
    timmy.forward(8)


screen = Screen()
screen.exitonclick()
