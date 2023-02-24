from turtle import Turtle


class Paddle(Turtle):
    user_location = (-350, 0)
    user2_location = (350, 0)

    def __init__(self):
        super().__init__()
        self.paddle = self.create_paddle()
        self.paddle.goto(self.user_location)
        self.paddle2 = self.create_paddle()
        self.paddle2.goto(self.user2_location)

    def create_paddle(self):
        paddle = Turtle("square")
        paddle.speed(0)
        paddle.color("white")
        paddle.shapesize(stretch_wid=4, stretch_len=1)
        paddle.penup()
        return paddle

    def up(self):
        x = self.paddle.xcor()
        y = self.paddle.ycor()
        y += 20
        self.paddle.goto(x, y)

    def user2_up(self):
        x = self.paddle2.xcor()
        y = self.paddle2.ycor()
        y += 20
        self.paddle2.goto(x, y)

    def down(self):
        x = self.paddle.xcor()
        y = self.paddle.ycor()
        y -= 20
        self.paddle.goto(x, y)

    def user2_down(self):
        x = self.paddle2.xcor()
        y = self.paddle2.ycor()
        y -= 20
        self.paddle2.goto(x, y)
