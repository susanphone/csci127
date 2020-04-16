# -----------------------------------------------------
# CSCI 127, Lab 10                                    |
# April 10, 2019                                       |
# Susan McCartney                                     |
# -----------------------------------------------------
# Using the class method and data structures
# focussed on stacks to go through a list of
# items and return was is "pushed" and what 
# is "popped."
class Stack:
    def __init__(self, name):
        #init stack class and create variables
        self.name = name
        self.items = []
    
    def push(self, num):
        #a method that pushes the stack
        self.items.append(num)

    def __iadd__(self, other):
        # Magic method that overrides the operator for n += 15
        self.items.append(other)
        return self.__str__()

    def pop(self):
        # A method that pops items from the stack
        return self.items.pop()

    def is_empty(self):
        # Boolean function used to determine if the stack is empty
        if len(self.items) == 0:
            return True

    
    def __str__(self):
        #str method for producing the right print format
        stack_contents = "Contents: "
        for num in self.items:
            stack_contents += str(num) + " "
        return stack_contents

# -----------------------------------------------------


def main():
    numbers = Stack("Numbers")

    print("Push 1, 2, 3, 4, 5")
    print("---------------------")
    for number in range(1, 6):
        numbers.push(number)
        print(numbers)

    print("\nPop one item")
    print("----------------")
    numbers.pop()
    print(numbers)

    print("\nPop all items")
    print("---------------")
    while not numbers.is_empty():
        print("Item popped:", numbers.pop())
        print(numbers)

    # Push 10, 11, 12, 13, 14
    for number in range(10, 15):
        numbers.push(number)

    # Push 15
    numbers += 15  # See: https://www.python-course.eu/python3_magic_methods.php
    print("\nPushed: 10, 11, 12, 13, 14, 15")
    print("-------------------------------")
    print(numbers)
# -----------------------------------------------------


main()
