from turtle import Turtle


class Scoreboard(Turtle):

    def refresh(self):
        self.clear()
        self.score += 1
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", move=False, align="center", font=('Courier', 15, 'bold'))

    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.ht()
        self.score = 0
        self.goto(0, 260)
