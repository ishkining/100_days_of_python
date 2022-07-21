from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.computer_score = 0
        self.player_score = 0
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.computer_score, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 200)
        self.write(self.player_score, align="center", font=("Courier", 40, "normal"))


    def point_to_computer(self):
        self.computer_score += 1
        self.update_scoreboard()

    def point_to_player(self):
        self.player_score += 1
        self.update_scoreboard()