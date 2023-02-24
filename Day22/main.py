import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Create the screen
screen = Screen()
screen.title("Ping Pong Game!")
screen.screensize(canvwidth=800, canvheight=600, bg="black")

# Create 2 paddles and allow users to move them
# Paddle 1 is moved up with up arrow key, down with down arrow key
# Paddle 2 is moved with w and s keys
user_paddle = Paddle()
screen.listen()
screen.onkeypress(user_paddle.up, "Up")
screen.onkeypress(user_paddle.user2_up, "w")
screen.onkeypress(user_paddle.down, "Down")
screen.onkeypress(user_paddle.user2_down, "s")

# Create the ball and make it move
ball = Ball()

# Create scoreboard
scoreboard = Scoreboard()

# Game logic
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with a paddle
    if ball.distance(user_paddle.paddle2) < 50 and ball.xcor() > 320 or ball.distance(user_paddle.paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # Detect when paddle misses (ball goes out of bounds)
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()
    # Keep score on left and right hand of screen

screen.exitonclick()
