# -----------------------------------------+
# Susan McCartney                          |
# CSCI 127, In Lab 1                       |
# -----------------------------------------|
# Modify an etch-a-sketch program.         |
# -----------------------------------------+
##read about onclick, onrealse, ondrag in turtle doc.

import turtle
import random

window = turtle.Screen()

pencil = turtle.Turtle()
pencil.speed(0)
square = turtle.Turtle()

# ---------------------------------

def draw_square(square):  
    square.up()
    square.goto(-200, 200)
    square.down()
    square.begin_fill()
    for i in range(3):
        square.forward(50)
        square.right(120)
    square.end_fill()

# ---------------------------------

def drawing_controls(x, y):
    if (-200 <= x <= -150) and (150 <= y <= 200):
        red = random.random()
        green = random.random()
        blue = random.random()
        pencil.color(red, green, blue)
        square.color(red, green, blue)      #added in
        draw_square(square)                 #added in

# ---------------------------------

def main():
    pencil.shape("circle")
    pencil.width(5)

    text = turtle.Turtle()
    text.hideturtle()
    text.up()
    text.goto(-205, 205)
    text.write("Change Color")

    square.speed(0)
    square.hideturtle()
    draw_square(square)

    window.onclick(drawing_controls)
    pencil.ondrag(pencil.goto)    
# ---------------------------------

main()
input("Press Enter to exit.")
