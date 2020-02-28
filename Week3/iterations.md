# Iterations:
## For-Loops:

#### Range Fuction:
    for i in range (0, 10, 1):
        print(i) OR print(i + 1)
        0               1
        1               2
        2               3
        3               4
        4               5
        5               6
        6               7
        7               8
        8               9
        9               10
    

for i in range(1, 11, 1):
    sum = sum + i
print(sum)

    1   2   3   4   5   6   7   8   9   10  55  
    = 5050

#### Not Range:
    for i in "Check...":
        print(i)
        C
        h
        e
        c
        k
        .
        .
        .

#### List:
    for i in [13, 7, "lucky number", 5]:
        i
    13
    7
    'lucky number'
    5

## While-Loops:
### Guess the Random Number
    import random
    answer = random.randint(1, 10):

    guess = 0
    while(guess != answer):

        guess = int(input("Guess the random number: "))
