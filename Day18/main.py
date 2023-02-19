import random
import turtle

import colorgram
from turtle import Turtle
from turtle import Screen


turtle.colormode(255)
rgb_colors = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)


#Paint a 10x10 painting of dots,
# pen size of 20
# spaces of 50 between dots

tom = Turtle()
tom.hideturtle()

x, y = tom.pos()

while y < 500:
    for _ in range(10):
        tom.pensize(20)
        tom.pendown()
        tom.dot(10,random.choice(rgb_colors))
        tom.penup()
        tom.forward(50)
    y += 50
    tom.setposition(x, y)

turtle.exitonclick()