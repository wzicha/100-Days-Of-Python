from turtle import Turtle


class Snake:
    # Create a snake body. Consists of 3 turtles (shaped as square), white colored, lined up together on the
    # horizontal axis Positioned as first one at 0,0 then next 20 px to left and other 20 px further to the left (no
    # overlap) Turtle has 20x20 px dimensions
    x_cord = [-40, -20, 0]
    # Segments keeps track of each part of the snakes' body
    segments = []

    def __init__(self):
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for x in self.x_cord:
            snake = Turtle("square")
            snake.speed("slowest")
            snake.color("white")
            snake.penup()
            snake.setx(x)
            self.segments.append(snake)
        return snake

    # Move the snake
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)
