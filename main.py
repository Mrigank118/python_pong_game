from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from Scoreboard import Score

import time

screen = Screen()
screen.tracer(0)
score = Score()
score.update()
# Screen Setup
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

# paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# ball
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()
    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.hit()
        score.increase_score_r()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.hit()
        score.increase_score_l()

    # detect when paddle misses
    if ball.xcor() > 420 or ball.xcor() < -420:
      game_is_on = False
      score.gameover()




screen.exitonclick()
