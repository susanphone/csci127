import turtle
window = turtle.Screen()

octagon = turtle.Turtle()
for i in range(8):
    octagon.forward(50)
    octagon.right(360/8)
    octagon.forward(50)

window.exitonclick()
