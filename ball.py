from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self, paddle):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # self.speed("slowest")
        self.initial_heading(paddle)

    def initial_heading(self, paddle):
        heading = random.randint(143, 217)
        if paddle.xcor() < 0:
            self.setheading(heading)
        else:
            self.setheading(heading + 180)

    def move(self):
        self.forward(1)

    def paddle_collision(self, paddle):
        if abs(self.xcor() - paddle.xcor()) < 20 and abs(self.ycor() - paddle.ycor()) < 80:
            new_heading = 180 - self.heading()
            self.setheading(new_heading)

    def wall_collision(self):
        if abs(self.ycor() - 300) < 10 or abs(self.ycor() + 300) < 10:
            new_heading = -self.heading()
            self.setheading(new_heading)

    def out_of_bounds(self):
        if abs(self.xcor()) > 410:
            return True
