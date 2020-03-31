# #Step 1:
# class Point:
#     """ Point class for representing and manipulating x,y coordinates. """

#     def __init__(self):
#         """ Create a new point at the origin """
#         self.x = 0
#         self.y = 0


# #Step 2
# class Point:
#     """ Point class for representing and manipulating x,y coordinates. """

#     def __init__(self):
#         """ Create a new point at the origin """
#         self.x = 0
#         self.y = 0


# p = Point()         # Instantiate an object of type Point
# q = Point()         # and make a second point

# print("Nothing seems to have happened with the points")


#Step 3
class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    def __init__(self):
	    """ Create a new point at the origin """
        self.x = 0
        self.y = 0

    p = Point()         # Instantiate an object of type Point
    q = Point()         # and make a second point

print("Nothing seems to have happened with the points")


# #Step 4
# class Point:
#     """ Point class for representing and manipulating x,y coordinates. """

#     def __init__(self):
#         """ Create a new point at the origin """
#         self.x = 0
#         self.y = 0

# p = Point()         # Instantiate an object of type Point
# q = Point()         # and make a second point

# print(p)
# print(q)

# print(p is q)

# #Step 5
# class Point:
#         """ Point class for representing and manipulating x,y coordinates. """
#     def __init__(self, initX, initY):
#         """ Create a new point at the given coordinates. """
#         self.x = initX
#         self.y = initY

# p = Point(7, 6)


# #Step 6
# class Point:
#     """ Point class for representing and manipulating x,y coordinates. """

#     def __init__(self, initX, initY):
#         """ Create a new point at the given coordinates. """
#         self.x = initX
#         self.y = initY

#     def getX(self):
#         return self.x

#     def getY(self):
#         return self.y

# #Step 7
# class Point:
#     """ Point class for representing and manipulating x,y coordinates. """

#     def __init__(self, initX, initY):
#         """ Create a new point at the given coordinates. """
#         self.x = initX
#         self.y = initY

#     def getX(self):
#         return self.x

#     def getY(self):
#         return self.y

#     def distanceFromOrigin(self):
#         return ((self.x ** 2) + (self.y ** 2)) ** 0.5


# p = Point(7, 6)
# print(p.distanceFromOrigin())



# #Step 8
# import math

# class Point:
#     """ Point class for representing and manipulating x,y coordinates. """

#     def __init__(self, initX, initY):
#         """ Create a new point at the given coordinates. """
#         self.x = initX
#         self.y = initY

#     def getX(self):
#         return self.x

#     def getY(self):
#         return self.y

#     def distanceFromOrigin(self):
#         return ((self.x ** 2) + (self.y ** 2)) ** 0.5

# def distance(point1, point2):
#     xdiff = point2.getX() - point1.getX()
#     ydiff = point2.getY() - point1.getY()

#     dist = math.sqrt(xdiff**2 + ydiff**2)
#     return dist

# p = Point(4, 3)
# q = Point(0, 0)
# print(distance(p, q))



# #Step 9
# class Point:
#     """ Point class for representing and manipulating x,y coordinates. """

#     def __init__(self, initX, initY):
#         """ Create a new point at the given coordinates. """
#         self.x = initX
#         self.y = initY

#     def getX(self):
#         return self.x

#     def getY(self):
#         return self.y

#     def distanceFromOrigin(self):
#         return ((self.x ** 2) + (self.y ** 2)) ** 0.5


# p = Point(7, 6)
# print(p)



# #Step 10
# class Point:
#     """ Point class for representing and manipulating x,y coordinates. """

#     def __init__(self, initX, initY):
#         """ Create a new point at the given coordinates. """
#         self.x = initX
#         self.y = initY

#     def getX(self):
#         return self.x

#     def getY(self):
#         return self.y

#     def distanceFromOrigin(self):
#         return ((self.x ** 2) + (self.y ** 2)) ** 0.5

#     def __str__(self):
#         return "x=" + str(self.x) + ", y=" + str(self.y)

# p = Point(7, 6)
# print(p)


# #Step 11
# class Point:

#     def __init__(self, initX, initY):
#         """ Create a new point at the given coordinates. """
#         self.x = initX
#         self.y = initY

#     def getX(self):
#         return self.x

#     def getY(self):
#         return self.y

#     def distanceFromOrigin(self):
#         return ((self.x ** 2) + (self.y ** 2)) ** 0.5

#     def __str__(self):
#         return "x=" + str(self.x) + ", y=" + str(self.y)

#     def halfway(self, target):
#          mx = (self.x + target.x) / 2
#          my = (self.y + target.y) / 2
#          return Point(mx, my)

# p = Point(3, 4)
# q = Point(5, 12)
# mid = p.halfway(q)

# print(mid)
# print(mid.getX())
# print(mid.getY())
