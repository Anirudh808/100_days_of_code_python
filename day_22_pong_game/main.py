from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Welcome to Pong!")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = ScoreBoard()


def r_paddle_up():
    new_y = r_paddle.ycor() + 20
    r_paddle.goto(r_paddle.xcor(), new_y)


def r_paddle_down():
    new_y = r_paddle.ycor() - 20
    r_paddle.goto(r_paddle.xcor(), new_y)


def l_paddle_up():
    new_y = l_paddle.ycor() + 20
    l_paddle.goto(l_paddle.xcor(), new_y)


def l_paddle_down():
    new_y = l_paddle.ycor() - 20
    l_paddle.goto(l_paddle.xcor(), new_y)


screen.listen()
screen.onkey(r_paddle_up, "Up")
screen.onkey(r_paddle_down, "Down")
screen.onkey(l_paddle_up, "w")
screen.onkey(l_paddle_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.xcor() > 330 and ball.distance(r_paddle) < 50 or ball.xcor() < -330 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # Detect when R misses the ball
    if ball.xcor() < -390:
        scoreboard.r_point()
        ball.restart()

    # Detect when L misses the ball
    if ball.xcor() > 390:
        scoreboard.l_point()
        ball.restart()


screen.exitonclick()
