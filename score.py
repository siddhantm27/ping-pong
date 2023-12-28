from turtle import Turtle


class Score(Turtle):

    def __init__(self, paddle):
        super().__init__()
        self.color("white")
        self.score = 0
        self.ht()
        self.penup()
        self.player_score_pos(paddle)
        self.refresh_score()

    def player_score_pos(self, paddle):
        x = paddle.xcor() / 7
        y = 250
        self.goto(x, y)

    def refresh_score(self):
        self.clear()
        self.penup()
        self.write(f"{self.score}", align="center",font=("Arial", 16, "normal"))
        self.penup()
