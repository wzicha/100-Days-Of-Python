from turtle import Turtle


class Paddle:
    user_locations = [(-440, 0), (-440, 20), (-440, 40), (-440, 60)]
    cpu_locations = [(440, 0), (440, 20), (440, 40), (440, 60)]

    def __init__(self):
        self.segment = []

    def create_user_paddle(self):
        for x in range(4):
            self.part = Turtle("square")
            self.part.speed(0)
            self.part.color("white")
            self.part.shapesize(stretch_wid=1, stretch_len=1)
            self.part.penup()
            self.part.goto(Paddle.user_locations[x])
            self.segment.append(self.part)

    def create_cpu_paddle(self):
        for x in range(4):
            self.part = Turtle("square")
            self.part.speed(0)
            self.part.color("white")
            self.part.penup()
            self.part.goto(Paddle.cpu_locations[x])
            self.segment.append(self.part)

    def up(self):
        self.segment.tracer(0)
        for i in range(len(self.segment) - 1, -1, -1):
            self.segment[i].setheading(90)
            self.segment[i].forward(20)
            x = self.segment[i - 1].xcor()
            y = self.segment[i - 1].ycor()
            self.segment[i].goto(x, y + 20)
        self.segment.update()

    def down(self):
        self.segment.tracer(0)
        for i in range(0, (len(self.segment)), 1):
            self.segment[i].setheading(270)
            self.segment[i].forward(20)
            x = self.segment[i - 1].xcor()
            y = self.segment[i - 1].ycor()
            self.segment[i].goto(x, y - 20)
        self.segment.update()

    def move_up(self):
        for i in range(len(self.segment)):
            x = self.segment[i].xcor()
            y = self.segment[i].ycor()
            if y < 320:
                self.segment[i].goto(x, y + 20)

    def move_down(self):
        for i in range(len(self.segment) - 1, -1, -1):
            x = self.segment[i].xcor()
            y = self.segment[i].ycor()
            if y > -320:
                self.segment[i].goto(x, y - 20)

