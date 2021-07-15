from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.write_score()

    def write_score(self):
        self.write(arg=f"Score : {self.score}", align="center", font=("Arial", 24, "normal"))

    def update(self):
        self.clear()
        self.score += 1
        self.write_score()

