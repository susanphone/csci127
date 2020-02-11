#base case do nothing
#solve the problem using smaller versions of the problem
def hanoi(disks, start, finish, hold):
    if disks >= 1:               #Base Case 0 - donothing
        #recursively move disks-1 disk from start to hold
        hanoi(disks-1, start, hold, finish)
        #move immediately disk "disks" from start to finish
        print("Move disk", disks, "from", start, "to", finish)
        #recursively move disks-1 disks from hold to finish
        hanoi(disks-1, hold, finish, start)


hanoi(5, "A", "C", "B")
