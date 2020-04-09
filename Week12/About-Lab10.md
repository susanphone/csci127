Data Structures called stacks and queues
    queue: first in first out
    stack: take from the top
For lab use stacks
enqueue is adding
dequeue is removing

class Queue:
    def __init__(self, name):
        self.name = name
        self.items = []

    def enqueue(self, num):
        self.items.append(num)

    def __iadd__(self, other): #override +=
        self.items.append(other)
        return self.__str__() #must return a way to print
    
    def dequeue(self):
        pass
    
    def is_empty(self):
        return True
    
    def __str__(self):
        return ""


Magic Methods
override an operator
