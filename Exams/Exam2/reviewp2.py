# Practice Practicum

#Question 1
#The missing function should return the number of lines that are contained in the file.
# Assume that the file exists and is located in the same directory as your python program.
# For example, if the file question1.txtcontains four lines, this output would be produced: 
# There are 4 lines in file question_one.tx

def count_lines(f):
    file = open(f, "r")
    count = 0
    for lines in file:
        count += 1
    return count

file_name = "question_one.txt"
how_many = count_lines(file_name)
print("There are", how_many, "lines in file", file_name)



#Question 2
#Supply the missing code below using good object oriented programming principles that minimize the size of the solution.  
# When the program runs, itshould generate the following output:
# A Car runs on gas
# A Truck runs on gas
# A Bicycle runs on pedal power

class Vehicle: #Superclass and use for inheritance
    def __init__(self, k):
        self.kind = k
        self.runs_on = "gas"

    def __str__(self):
        return "A " + self.kind + " runs on " + self.runs_on

class Bicycle(Vehicle):
    def __init__(self):
        Vehicle.__init__(self, "Bicycle")#"Bicycle" is the Vehicle class #has to come first in subclass
        # self.kind = "Bicycle"           #instance variable
        self.runs_on = "pedal power"
    # def __str__(self):
        # return "A Bicycle runs on pedal power."


def main(): 
    car = Vehicle("Car")
    print(car)          #use __str__
    truck = Vehicle("Truck")
    print(truck)
    bicycle = Bicycle()
    print(bicycle)
main()


