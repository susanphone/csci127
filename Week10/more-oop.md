# Monday Lecture

### go over blender.py
### method is a function inside of a class
    __init__ method called whenever you invoke the class
    my_blender is a defined object of type blender
    Blender is a method
    Blender("green", "Ninja", 48)
        this is user by calling __init__
    self is referring to my_blender
    self.(variable) is a way we can access certain attributes
### (he changed the blender.py code since last time) (fixit)
    __str__(self):
    print(my_blender)
#### the __str__ is special syntax that will know to call this method
## Inheritance
    object can have level of how specific you can get
    method: turn_on
    property: is_on

            appliance
            /        \
        blender      toaster
            |           |
        volume         width of toast
    attributes: name and age    (chukie, 2)
    method: is_sleeping         (boolean variable)
                pets
            /     |     \
          dog    fish   rock
          |       |       |
        breed   water   color
_______________________________________
        brush() clean_filter() paint()
## Class Pet
    class Pet:
        def __init__(self, n, a, s):
            self.name = n
            self.age = a
            self.is_sleeping = s
        
        def set_name(self, n):
            self.name = n
        
        def set_age(self, a):
            self.age = a
        
        def set_is_sleeping(self):
            self.is_sleeping = s
        
        def __str__(self):
            return self.name + " is " + str(self.age) + " years old."
    
    my_pet = Pet("Dan's Pet", 0, False)
    print(my_pet)

    >>> Dan's Pet is 0 years old.
### __str__ without this the string method is undefined.
### making methods into verbs makes it easier to follow
## Adding pets
    class Pet:
        def __init__(self, n, a, s):
            self.name = n
            self.age = a
            self.is_sleeping = s
        
        def set_name(self, n):
            self.name = n
        
        def set_age(self, a):
            self.age = a
        
        def set_is_sleeping(self):
            self.is_sleeping = s
        
        def __str__(self):
            return self.name + " is " + str(self.age) + " years old."
    
    class Dog(Pet): #breed attribute and brush method were added

        def __init__(self, name, age):
            Pet.__init__(self, name, age)
            self.breed = "Unknown"
        
        def brush(self):
            print("Arf! Thanks for the dog brushing!")
    
    my_pet = Pet("Dan's Pet", 0, False)
    print(my_pet)
    """
    my_dog = my_pet
    my_dog.set_name("Chuki")
    my_dog.set_age(2)
    print(my_dog)
    >>> Chuki is 2 years old.
    my_dog.brush()
    """
## Assigning my_dog
    class Dog(Pet): #breed attribute and brush method were added

        def __init__(self, name, age, sleep, b):
            Pet.__init__(self, name, age, sleep)
            self.breed = b
        
        def brush(self):
            print("Arf! Thanks for the dog brushing!")
    my_dog = Dog("Chuki", 2, True, "Giant Chiuaua")
    print(my_dog)
    my_dog.brush()

    my_pet.brush()
    >>> Chuki is 2 years old
        Arf! Thanks for the dog brushing!
## The rest of the pets
    class Pet:
        def __init__(self, n, a, s):
            self.name = n
            self.age = a
            self.is_sleeping = s
        
        def set_name(self, n):
            self.name = n
        
        def set_age(self, a):
            self.age = a
        
        def set_is_sleeping(self):
            self.is_sleeping = s
        
        def __str__(self):
            return self.name + " is " + str(self.age) + " years old."
    
    class Dog(Pet):

        def __init__(self, name, age, sleep, b):
            Pet.__init__(self, name, age, sleep)
            self.breed = b
        
        def brush(self):
            print("Arf! Thanks for the dog brushing!")
    
    class Fish(Pet):
        def __init__(self, name, age, sleep, sw):
        Pet.__init__(self, name, age, sleep)
        self.salt_water = sw

    def change_filter(self):
        print("Glug! Thanks for changing the filter.")

    class Rock(Pet):

        def __init__(self, name, age, sleep, c):
            Pet.__init__(self, name, age, sleep)
            self.color = c

        def set_paint(self, c):
            self.color = c

        def __str__(self):
            return Pet.__str__(self) + "It's " + self.color
    
    my_pet = Pet("Dan's Pet", 0, False)
    print(my_pet)

    my_dog = Dog("Chuki", 2, True, "Giant Chiuaua")
    print(my_dog)
    my_dog.brush()

    #my_pet.brush()

    my_fish = Fish("Steve", 14, True, False)
    print(my_fish)
    my_fish.change_filter()

    my_rock = Rock("Rocky", 1000000000, True, "gray")
    print(my_rock)
    my_rock.set_paint("red")
    print(my_rock)

    >>>Dan's Pet is 0 years old.
        Chuki is 2 years old.
        Arf! Thanks for the dog brushing!
        Steve is 14 years old.
        Glug! Thanks for changing the filter.
        Rocky is 1000000000 years old. It's gray.
        Rocky is 1000000000 years old. It's red.

## Next time learn about inheritance and dungeons and dragons. Dungeons.py





