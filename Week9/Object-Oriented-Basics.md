# Object Oriented Programming
## Think of the data and the functions are a package deal.
    The Turtle is an object
    Methods are functions that go with an object
        turtle.Turtle() is a constructor method
        Methods include the name of the object
        Also include the object dot method(argument) (cross.forward(100))
    string.lower works but turtle.lower doesn't work
    file.readline()
    lists
    dictionaries
    ....anything can be an object!
## Objects with special types of data
## Methods are made unique for each functions.

# Paradigm: A way of Thinking
## Procedural:
    A function is aprocedure: a thing to be done
    We can send an object to a procedure
    The procedure can use the object to get the job done
        do_thing(my_object, 5)

## Object Oriented:
    A function is assicoated with an object; now call it a method
    The object can call its method with the .(dot) operator
    The object can use the method to get the job done
        my_object.do_thing(5)

### Syntax is different
        Procedural                Object Oriented
    do_thing(my_object(5)       my_object.do_thing(5)

## Object Oriented Method is coding the same way we look at the world!
### Objects do things
    A blender blends
    my_blender.blend(5)
        Objects > Methods > Data
        blender > blend   > fruits
    objects- blender
    methods - blend setting
        def blend(setting):
            print("blending on", setting)
            return smoothie

    my_smoothie = my_blender.blend(5)
    my_smoothie.drink()
### Class: is a type of object


