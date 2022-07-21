from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.up()
        self.color("white")
        self.increment_x = 10
        self.increment_y = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.increment_x, self.ycor() + self.increment_y)