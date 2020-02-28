days = ['mon', 'tue', 'wed', 'thur', 'fri']
#Iterative Methods
def reverseList(alist):
    result = []
    #pure function
    for i in range(len(alist)):
        #start at the end and go back toward the beginning.
        result.append(alist[(len(alist)-1)-i])
    return result
print(reverseList(days))

def reverseList2(alist):
   for i in alist:
       result = [item] + result
    return result

#Recursive Method
def recursiveReverseList(alist):
    if alist == []:
        return alist
    else:
        return recursiveReverseList(alist[1:]) + [alist[0]]
#Recursive function recursiveReverseLIst works by SPLITTING alist by first taking off monday, then running the function again and taking off
#tuesday, it will run again and take off wednesday, then 
#run again and take off thursday, finally if will run again
#will add Friday to the result. Putting friday at the
#beginning of the list. After that it will go through the
#list starting at monday and end at thursday, add thursday
#to the list. The list will end up looking like this:
# [fri, thur, wed, tue, mon]
#once the program adds Tuesday and goes back to monday
# it will finally add monday to the list after passing 
#monday four times in this program.