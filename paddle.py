from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color("white")
        self.setheading(90)

    def pos_player1(self):
        self.penup()
        self.goto(x=-350, y=0)

    def pos_player2(self):
        self.penup()
        self.goto(x=+350, y=0)

    def player_up(self):
        self.forward(20)

    def player_down(self):
        self.backward(20)

