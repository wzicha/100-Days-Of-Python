import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")

player = Player()

screen.listen()
screen.onkeypress(player.up, "Up")

car = CarManager()
car.hideturtle()
counter = 0

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    counter += 1
    # Create a new car every 6th time the loop runs
    if counter == 6:
        car.create_car()
        car.hideturtle()
        counter = 0
    car.move_cars()
    # Detect when the turtle player collides with a car
    for car_object in car.cars:
        if player.distance(car_object) < 20:
            print("GAME OVER!")
        # When the turtle hits a car, GAME OVER should be displayed in the centre.
            player.game_over()
        # Stop the game if this happens
            game_is_on = False
    # Detect when the turtle player has reached the top edge of the screen
    if player.ycor() >= 280:
        scoreboard.increase()
    # When this happens, return the turtle to the starting position
        player.start()
    # Increase the speed of the cars
        car.level_up()
