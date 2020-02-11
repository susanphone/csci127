
import turtle
import random

window = turtle.Screen()

drawer = turtle.Turtle()
drawer.speed(0)

def east():
    drawer.setheading(random.randrange(-5,6,1))
    drawer.forward(random.rangrange(50,60,1))

def north():
    drawer.setheading(90)
    drawer.forward(50)

def west():
    drawer.setheading(180)
    drawer.forward(50)

def south():
    drawer.setheading(270)
    drawer.forward(50)

window.onkey(east, "d")
window.onkey(north, "w")
window.onkey(west, "a")
window.onkey(south, "s")
window.listen()

window.exitonclick()