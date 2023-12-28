from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)

paddle1 = Paddle()
paddle1.pos_player1()
paddle2 = Paddle()
paddle2.pos_player2()
ball = Ball(paddle1)
scoreboard1 = Score(paddle1)
scoreboard2 = Score(paddle2)

line = Turtle()
line.goto(x=0, y=-300)
line.speed("fastest")
line.pencolor("white")
line.left(90)
for i in range(0, 30):
    line.forward(20)
    line.penup()
    line.forward(20)
    line.pendown()

screen.update()

screen.listen()
screen.onkeypress(key="w", fun=paddle1.player_up)
screen.onkeypress(key="s", fun=paddle1.player_down)
screen.onkeypress(key="Up", fun=paddle2.player_up)
screen.onkeypress(key="Down", fun=paddle2.player_down)

game = True
while game:
    if ball.out_of_bounds():
        if ball.xcor() > 0:
            ball = Ball(paddle1)
            scoreboard1.score += 1
            scoreboard1.refresh_score()
        elif ball.xcor() < 0:
            ball = Ball(paddle2)
            scoreboard2.score += 1
            scoreboard2.refresh_score()
    ball.move()
    time.sleep(0.003)
    ball.paddle_collision(paddle1)
    ball.paddle_collision(paddle2)
    ball.wall_collision()
    screen.update()

screen.exitonclick()
