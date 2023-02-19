import random
from turtle import Turtle
from turtle import Screen

screen = Screen()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
Turtles = []

screen.title("Turtle Race")
#Create pop-up on Screen which asks user to select a turtle
selection = screen.textinput("Who will be the winner?", "Pick a turtle: ")

#Initialize screen, of specific x and y values
screen.setup(500, 500, 0, 0)

#Create six different positions to spread out the turtles
positions = [-450, -250, -50, 150, 350, 475]

#Create 6 turtles, all of random colors
for color in range(0,6):
  Tim = Turtle()
  Tim.penup()
  Tim.shape("turtle")
  Tim.color(colors[color])
  Tim.goto(-450, positions[color])
  Turtles.append(Tim)

race_on = True

while race_on:
    for turtle in Turtles:
       if turtle.xcor() >= 500:
        race_on = False
        winner = turtle.pencolor()
        print(f"The winner is {winner}. You selected {selection}")
        if winner == selection:
          print(f"Congratulations! You won!!!")
        break
       turtle.forward(random.randint(0,100))

screen.bye()




