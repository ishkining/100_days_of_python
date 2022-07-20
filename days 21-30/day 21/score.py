from turtle import Turtle

# TODO: 5: Create a scoreboard
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.score += 1
        self.color("white")
        self.up()
        self.goto(-20, 270)
        self.shape("classic")
        self.write(f"Score = {self.score}", True, align="center", font=("Arial", 12))
        self.color("black")

    def game_over(self):
        self.color("white")
        self.up()
        self.goto(0, 0)
        self.write("Game Over!", True, align="center", font=("Arial", 12))
