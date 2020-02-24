# Turtle
Turtle is the name of the Module
        Turtle type         turtle.Turtle()
        Screen type         turtle.Screen()
Canvas is the window to draw on.
#### Turtle begins by facing EAST unless directions specify otherwise.
    Window Background Color     wn.bgcolor
    Turtle's assigned name      alex = turtle.Turtle()
    Color of turtle             alex.color("blue)
    Size of pen                 alex.pensize(3)
    Exit window                 wn.exitonclick()
Control flow until now has been strictly top to bottom, one statement at a time. We call this type of control sequential. In Python flow is sequential as long as successive statements are indented the same amount. The for statement introduces indented sub-statements after the for-loop heading.

##### Direction of Turtle:
    Up          turtle.up()- lifts turtle

    Down        turtle.down()- drops turtle

    Shape       turtle.shape()- designates a 
                specific shape 
                arrow, blank, circle, classic, 
                square, triangle, turtle

    Speed       turtle.speed(0)- (0-10)

    Stamp       turtle.stamp()- stamps the 
                shape of the turtle


### Methods

    Method                   Parameters         
    Description

    Turtle                     None             Creates and returns a new turtle object

    forward                    distance         Moves the turtle forward

    backward                   distance         Moves the turle backward

    right                      angle            Turns the turtle clockwise

    left                       angle            Turns the turtle counter clockwise

    up                         None             Picks up the turtles tail

    down                       None             Puts down the turtles tail

    color                      color name       Changes the color of the turtle’s tail

    fillcolor                  color name       Changes the color of the turtle will use to fill a polygon

    heading                    None             Returns the current heading

    position                   None             Returns the current position

    goto                       x,y              Move the turtle to position x,y

    begin_fill                 None             Remember the starting point for a filled polygon

    end_fill                   None             Close the polygon and fill with the current fill color

    dot                        None	         Leave a dot at the current position

    stamp	                   None	         Leaves an impression of a turtle shape at the current location

    shape                      shape name       Should be ‘arrow’, ‘classic’, ‘turtle’, ‘circle’ or ‘square’
