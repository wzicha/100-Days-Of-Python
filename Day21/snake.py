from turtle import Turtle


class Snake:
    # Create a snake body. Consists of 3 turtles (shaped as square), white colored, lined up together on the
    # horizontal axis Positioned as first one at 0,0 then next 20 px to left and other 20 px further to the left (no
    # overlap) Turtle has 20x20 px dimensions
    # Segments keeps track of each part of the snakes' body
    segments = []

    def __init__(self):
        self.positions = [(0, 0), (-20, 0), (-40, 0)]
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in self.positions:
            self.add_segment(position)

    # Move the snake
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.speed("slowest")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setpos(position)
        self.segments.append(new_segment)

    # Extend the snake when eating a fruit
    def extend(self):
        self.add_segment(self.segments[-1].position())

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
