from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, player):
        super().__init__("square")
        self.speed("fastest")
        self.up()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(350 * (player if player == 1 else -1), 0)
        self.speed("normal")
        self.computer_step = 30

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)

    def computer_move(self):
        if self.ycor() > 260 or self.ycor() < -260:
            self.computer_step *= -1
        self.goto(self.xcor(), self.ycor() + self.computer_step)