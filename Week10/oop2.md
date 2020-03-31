# Wednesday Lecture
### go over pet.py and Inheritance
# Universal Modeling Language (UML)
## Pet.py
     class Pet:
        def __init__(self, n, a, s):        #instance variable
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

        def __init__(self, name, age, sleep, b):        #super class
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
        
        def main():
            my_pet = Pet("Dan's Pet", 0, False)
            print(my_pet) #use __str__ method

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
        
        main()

    >>> Dan's Pet is 0 years old.
        Chuki is 2 years old.
        Arf! Thanks for the dog brushing!
        Steve is 14 years old.
        Glug! Thanks for changing the filter.
        Rocky is 1000000000 years old. It's gray.
        Rocky is 1000000000 years old. It's red.

## Mutable Object Orientation:
### Change an object by using it's methods
    Fractions example in textbook
    Dungeons and Dragons
## UML of Dungeons and Dragons
###            Character
    instance variables: intelligence, strength...
    methods: __init__(), __str__(), get_intelligence(), get_strength(), set_intelligence(), set_strength()...
        /                   \
####  Human                 Orc
        race                race
        __init__()        __init__()
                            less intelligence and charisma
                            more strength

## Program 4
    

