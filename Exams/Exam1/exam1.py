# cost = input("Enter the cost of groceries: ")   #correct
# payment = int(float(cost)/20)                   #only needed float
# if payment is not int:        #this if statement                        
#     payment += 1                #is not needed
# change = -(float(cost) - int(payment*20))       #bills = (cost//20) + 1
# print(int(payment))                             #change = (bill*20) - cost
# print("Pay with " + str(payment) + " twenties, and get back " + str(change)) #correct

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
    redCross.right(90)          #needed to hide the turtle (5)
redCross.end_fill()
window.exitonclick()

# user_input = input("Enter numbers separated by spaces: ")
# nums = user_input.split()

# def print_progression(nums):        #(prog)
#     nums.sort()                     
#     for i in range(len(nums)):    
#         if i is -1:
#            return nums
#         if i < 0 or i is 0:
#            nums = " -> ".join(nums)
#     return nums

# print(print_progression(nums))

