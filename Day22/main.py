from turtle import Turtle, Screen
from paddle import Paddle

# Create the screen
screen = Screen()
screen.title("Ping Pong Game!")
screen.screensize(canvwidth=800, canvheight=600, bg="black")


# Create and move a paddle
 # is 4 turtles huddled together. User is on left hand side, computer on the right
 # Paddle is moved up with up arrow key, down with down arrow key
user_paddle = Paddle()
user_paddle.create_user_paddle()
screen.listen()
screen.onkeypress(user_paddle.up, "Up")
screen.update()
screen.onkeypress(user_paddle.down, "Down")

# Create another paddle
 # Paddle can only move along y-axis, random movement
cpu_paddle = Paddle()
cpu_paddle.create_cpu_paddle()

# Create the ball and make it move
 # Make it move randomly toward left or right

# Detect collision with wall and bounce

# Detect collision with a paddle

# Detect when paddle misses

# Keep score
 # On left and right hand of screen

screen.exitonclick()
