from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 80 and ball.xcor() > 330 or ball.distance(l_paddle) < 80 and ball.xcor() < -330:
        ball.bounce_x()

    #Detect when right paddle misses
    elif ball.xcor() > 380:
        ball.ball_reset()
        scoreboard.l_point()

    # Detect when left paddle misses
    elif ball.xcor() < -380:
        ball.ball_reset()
        scoreboard.r_point()



screen.exitonclick()