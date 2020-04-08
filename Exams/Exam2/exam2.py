#1.
# myfile = open("question_one.txt", "r")
# line_list = myfile.split()
# for line in range(0,len(line_list),2):
#     print(line, end ='')
#myfile.close()
    
#2.
# myfile = open("question_one.txt", "r")
# my_list = myfile.readline()
# print(my_list)

#3.
#file = open("filename", "w")
#to write in a file


#4.
# inventory = {"Red Battleships":55, "Earth-like planets":40, "Knives":1, "Spoons":1, "Forks":1, "Tears in my eye":0}
# print("Rolls" in inventory)
# print(inventory["Tears in my eye"] == 0)
# print(inventory.get("Forks"))
# print(inventory["Knives"])
# print(len(inventory))

#5.
# inventory = {"Red Battleships":55, "Earth-like planets":40, \
# "Knives":1, "Spoons":1, "Forks":1, "Tears in my eye":0}
# for v in inventory:
#     if inventory[v] == 1:
#         print(v)

#6.
class Skier:
    def __init__(self, first, cm, pounds, skill, where):
        self.name = first
        self.height = cm
        self.weight = pounds
        self.ability = skill
        self.location = where

    def set_location(self, where):
        self.location = where

    def __str__(self):
        n = "Name: " + str(self.name) + "\n"
        h = "Height: " + str(self.height) + " cm \n"
        w = "Weight: " + str(self.weight) + " lbs. \n"
        a = "Ability: " + str(self.ability) + "\n"
        l = "Location: " + self.location + "\n"
        return n + h + w + a + l


class Tourist(Skier):
    def __init__(self, first, inches, cm, skill):
        Skier.__init__(self, first, inches, cm, skill, "Lodge")

    def __str__(self):
        return Skier.__str__(self)


class ParkRat(Skier):
    def __init__(self, first, inches, cm, skill):
        Skier.__init__(self, first, inches, cm, skill, "Terrain park")

    def __str__(self):
        return Skier.__str__(self) + "Clothing: baggy \n"


def main():
    jack = Skier("Jack", 160, 140, 4, "Papa Bear")
    print(jack)
    jerry = Tourist("Jerry", 74, 240, 1)
    print(jerry)

main()


# import numpy as np
# myarray = np.array([5, 10, 15])
# print(myarray)


# import numpy as np
# myarray = np.zeros((2, 3))
# print(myarray)

# import numpy as np
# a = np.random.randint(10, 50, size=(2, 6))
# print(a)
# # a[1] = a[1]*2
# a= a.reshape((4,3))
# print(a)
# a[1] = a[1]*2
# print(a)
