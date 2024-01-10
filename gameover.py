from turtle import Turtle


class Gameover(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.ht()
        self.write("Game Over", move=False, align="center", font=('Courier', 20, 'bold'))
