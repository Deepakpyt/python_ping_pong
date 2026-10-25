from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("Pong")
my_screen.tracer(0)

paddle = Paddle(350)
paddle2 = Paddle(-350)
pong = Ball()
score = Scoreboard()


my_screen.listen()
my_screen.onkey(paddle.up, "Up")
my_screen.onkey(paddle.down, "Down")
my_screen.onkey(paddle2.up, "w")
my_screen.onkey(paddle2.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(pong.move_speed)
    my_screen.update()
    pong.move()

    # Detect collision with wall
    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce_y()
    # Detect the paddle
    if pong.distance(paddle) < 50 and pong.xcor() > 320 or pong.distance(paddle2) < 50 and pong.xcor() < -320:
        pong.bounce_x()
    # Detect a paddle misses the ball.
    if pong.xcor() > 380:
        pong.reset()
        score.l_point()

    if pong.xcor() < -380:
        pong.reset()
        score.r_point()

my_screen.exitonclick()
