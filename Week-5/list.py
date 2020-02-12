yourlist = [1, -3, -5, 8]

#define the function
def sum_negatives(yourlist):
    neg_sum = 0
    for num in yourlist:
        if num < 0:
            neg_sum += num
        print(neg_sum)
#GOAL: give back the negative number

#call the function
x = sum_negatives(yourlist)
print(x)
#converting the function
