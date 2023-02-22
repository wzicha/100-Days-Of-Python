import random
from turtle import Turtle


class Food(Turtle):

    # Food class, snake increases in size when it is consumed
    # Render itself as a small circle on the screen

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
