##A hexagon (six sides)

import turtle 
wn = turtle.Screen()
alex = turtle.Turtle()
alex.shape("turtle")
alex.pensize(3)

for i in range(6):
    alex.forward(90)
    alex.left(60)