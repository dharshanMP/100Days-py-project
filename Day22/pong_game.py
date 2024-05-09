from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time


screen = Screen()
ball = Ball()
scoreboard = Scoreboard()

screen.setup(width = 800, height = 600)
screen.bgcolor("gray10")
screen.setup()
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((320 , 0))
left_paddle = Paddle((-320, 0))

screen.listen()
screen.onkey(right_paddle.upward, "Up")
screen.onkey(right_paddle.downward, "Down")
screen.onkey(left_paddle.upward, "a")
screen.onkey(left_paddle.downward, "s")




game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()


    # collision on the wall
    if ball.ycor() > 270 or ball.ycor() < - 270:
        ball.bounce_y()


    # collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 300 or ball.distance(left_paddle) < 50 and ball.xcor() -300:
        ball.bounce_x()


    # ball out of right_paddle
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.left_point()

    # left_paddle
    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.right_point()


screen.exitonclick()