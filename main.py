
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=800, height=600)
my_screen.title("ping pong game")

my_screen.tracer(0)

r_paddle = Paddle((380, 0))

l_paddle = Paddle((-380, 0))

ball = Ball()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(fun=r_paddle.go_up, key="Up")
my_screen.onkey(fun=r_paddle.go_down, key="Down")
my_screen.onkey(fun=l_paddle.go_up, key="w")
my_screen.onkey(fun=l_paddle.go_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    my_screen.update()
    ball.move()
    # detect collisions with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect collisions with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect missing bounds
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset()

        scoreboard.r_point()

my_screen.exitonclick()
