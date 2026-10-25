from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor):
        self.given_x = x_cor
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_cor, 0)

    def up(self):
        y = self.ycor()
        self.goto(self.given_x, y + 20)

    def down(self):
        y = self.ycor()
        self.goto(self.given_x, y - 20)

