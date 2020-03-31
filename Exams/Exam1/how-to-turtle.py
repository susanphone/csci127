# Write a function to make an octagon
import turtle


def draw_polygon(polygon, sides, length):
    for side in range(sides):
        polygon.forward(length)
        polygon.left(360 - (360 / sides))  # <------ can draw any polygon


def create_turtle(turtle_color, x, y):
    generic_turtle = turtle.Turtle()
    generic_turtle.hideturtle()
    generic_turtle.up()
    generic_turtle.goto(x, y)
    generic_turtle.down()
    generic_turtle.color(turtle_color)
    return generic_turtle


window = turtle.Screen()

octagon = create_turtle("red", 100, 100)
draw_polygon(octagon, 8, 50)

square = create_turtle("blue", -250, -77)
draw_polygon(square, 4, 100)

window.exitonclick()


#draw a star using turtle graphics.

import turtle
window = turtle.Screen()

points = 7
angle= 180 - (180 / points)
star = turtle.Turtle()
star.speed(10)
star.hideturtle()
star.backward(50)
#star.goto(-50, 0)

for i in range(points):
    star.forward(100)
    star.right(angle)

window.exitonclick()


