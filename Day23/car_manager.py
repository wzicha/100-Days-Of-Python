import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left
# edge of the screen.

# No cars should be generated in the top and bottom 50px of the screen
# Restrict car creation from y -250 to 250. Cars created at x 300

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.goto(300, random.randint(-250, 250))
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


