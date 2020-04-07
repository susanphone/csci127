# files
    open:           file = open(filename, "r")
    close:          file.close()
    constructor:
    reader:
    writer:
## Run a for loop in files:
### method 1: counting method
    num = 0
    for line in file:
        num += 1
        print(num, line, end="")
### method 2: using a list
    fileliist = file.readlines():
    for i in range(len(filelist)):
        print(i+1, filelist[i], end="")



# Dictionaries
    Reorder the code to create a dictionary output like this:
        1{'apples':15, 'bananas':35, 'grapes':12}
        2{'apples':15, 'bananas':35, 'grapes':12, 'oranges':20}
        3{'bananas':35, 'grapes':12, 'oranges':20}
        35
        3

   1. d = {'apples':15, 'bananas':35, 'grapes':12}
   2. print(d)
   3. d['oranges']= 20
   4. print(d)
   5. del d['apples']
   6. print(d)
   7. print(d['bananas'])
   8. print(len(d))
   

# Object Oriented Programming

### defining each term from program
    __init__():    def __init__(self, k)        initalializing the instance variables
    constructor:   car = Vehicle("Car")         constructor for the Vehicle class
    object(instance):        car or truck                 Object vehicle with instance car
    class:         class Vehicle                
    inheritance:   class Bicycle(Vehicle)
### example program
    class Vehicle:
    def __init__(self, k):
        self.kind = k
        self.runs_on = "gas"
    def __str__(self):
        return "A " + self.kind + " runs on " + self.runs_on

    class Bicycle(Vehicle):
        def __init__(self):
            Vehicle.__init__(self, "Bicycle")
            # self.kind = "Bicycle"           
            self.runs_on = "pedal power"

    def main(): 
        car = Vehicle("Car")
        print(car)          
        truck = Vehicle("Truck")
        print(truck)
        bicycle = Bicycle()
        print(bicycle)
    main()
### More terms:
    __str__
    __add__
    Inheritance
    Encapsulation
    Polymorphism



# Numpy
### Arrays:
### ndarrays:
### arrange:
### reshape:


# Review
    String      a = "1, 2, 3, 4"
    Tuple       a = (1, 2, 3, 4)
    List        a = [1, 2, 3, 4]
    Object      a = A(1, 2, 3, 4)
    Numpy       a = np.array([1, 2, 3, 4])