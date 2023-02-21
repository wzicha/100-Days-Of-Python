import time
from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

# Listen to user inputs to control the snake
screen.listen()
screen.onkey (snake.up, "Up")
screen.onkey (snake.down, "Down")
screen.onkey (snake.left, "Left")
screen.onkey (snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

# Create snake food


# Detect collision with food

# Create a scoreboard


# Detect collision with wall


# Detect collision with tail


screen.exitonclick()
