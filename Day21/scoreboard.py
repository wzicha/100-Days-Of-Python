import random
import turtle
from turtle import Turtle
from food import Food


class Scoreboard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        # Clear the scoreboard every time the snake gets a fruit
        self.write(f"Current Score = {Scoreboard.score} ", False, align="center",
                   font=('Times New Roman', 16, 'bold'))

    def increase(self):
        Scoreboard.score += 1
        # Increment score by one each time the snake eats a fruit
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align="center", font=('Times New Roman', 16, 'bold'))
