from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.snake_body = []
        for iterator in range(3):
            self.add_segment(0 - (iterator * 20), 0)

    def move(self):
        for segment in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[segment].goto(self.snake_body[segment - 1].xcor(), self.snake_body[segment - 1].ycor())
        self.snake_body[0].forward(20)

    def up(self):
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)

    def down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)

    def left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def add_segment(self, positionx, positiony):
        new_turtle = Turtle()
        new_turtle.up()
        new_turtle.shape('square')
        new_turtle.color('white')
        new_turtle.goto(positionx, positiony)
        self.snake_body.append(new_turtle)

    def extend_segment(self):
        self.add_segment(self.snake_body[-1].xcor(), self.snake_body[-1].ycor())
