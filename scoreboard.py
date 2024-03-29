from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.write(f"Score:{self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} Highscore: {self.highscore}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            with open("data.txt", "w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GameOver", align=ALIGNMENT, font=FONT)