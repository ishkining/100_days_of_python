from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__("turtle")
        self.up()
        self.color("blue")
        self.start_position()
        self.setheading(90)

    def move_forward(self):
        self.forward(10)

    def is_turtle_reached(self):
        return self.ycor() >= FINISH_LINE_Y

    def start_position(self):
        self.goto(STARTING_POSITION)
