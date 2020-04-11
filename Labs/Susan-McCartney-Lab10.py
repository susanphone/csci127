# -----------------------------------------------------
# CSCI 127, Lab 10                                    |
# April 9, 2019                                       |
# Susan McCartney                                     |
# -----------------------------------------------------

# Your solution goes here.  Do not change anything below.
class Stack:
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def push(self, num):
        self.items.append(num)

    def __iadd__(self, other):
        self.items.append(other)
        return self.__str__()

    def pop(self):
        return self.items.pop()
        # return "Item popped: " + self.__str__()

    def is_empty(self):
        if len(self.items) == 0:
            return True

    
    def __str__(self):
        # item_lis = self.items
        # for items in range(item_lis):
        #     item_list += items + " "
        return "Contents: " + str(self.items)

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
        print("In while. ", numbers)

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
