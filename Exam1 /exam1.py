cost = input("Enter the cost of groceries: ")
payment = int(float(cost)/20)
if payment is not int:
    payment += 1
change = -(float(cost) - int(payment*20))
print(int(payment))
print(change)

import turtle
window = turtle.Screen()
redCross = turtle.Turtle()
redCross.color("red")
redCross.fillcolor("red")
redCross.begin_fill()
for i in range(4):
    for i in range (2):
        redCross.forward(100)
        redCross.left(90)
    redCross.forward(100)
    redCross.right(90)
redCross.end_fill()
window.exitonclick()

# user_input = input("Enter numbers separated separated by spaces: ")
# nums = user_input.split()
# def print_progression(nums):
#     nums.sort()
#     for i in range(len(nums)):
#         if i is -1:
#            return nums
#         if i < 0 or i is 0:
#            nums = " -> ".join(nums)
#     return nums

# print(print_progression(nums))

