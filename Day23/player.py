from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress
# to move the turtle north.

class Player(Turtle):
    FONT = ("Courier", 24, "normal")

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.right(270)
        self.start()

    def start(self):
        self.goto(STARTING_POSITION)

    def up(self):
        x = self.xcor()
        y = self.ycor()
        y += 20
        self.goto(x, y)

    def game_over(self):
        dead_turtle = Turtle()
        dead_turtle.hideturtle()
        dead_turtle.penup()
        dead_turtle.goto(0, 0)
        dead_turtle.write("Game OVER", False, align='Center', font=Player.FONT)

