from turtle import Turtle


# Create a scoreboard that keeps track of which level the user is on.

# Every time the turtle player does a successful crossing, the level should increase.

class Scoreboard(Turtle):
    FONT = ("Courier", 24, "normal")

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-210, 260)
        self.level = 0
        self.write(f"Level: {self.level}", False, align='Center', font=Scoreboard.FONT)

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", False, align='Center', font=Scoreboard.FONT)

    def increase(self):
        self.level += 1
        self.update()
