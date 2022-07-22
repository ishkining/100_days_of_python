from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.up()
        self.goto(-220, 250)
        self.update_score(1)
        self.hideturtle()

    def update_score(self, level):
        self.clear()
        self.write(f"Level {level}", align="center", font=FONT)
