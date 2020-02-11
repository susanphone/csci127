# Recursion

### Repeat the same fuction; A fuction that calls itself

Example: Fractal, Tower of Hanoi, Folders within folders.

## Laws of Recursion:

1. A recursive algorithm must have a BASE CASE.

2. Has to change it's state and move towards the base case.

3. Algorithm must call itself

#### Recursion needs a way out of the function.:
    while(True):
    
        print("This could take awhile...")
    def check_it_out():
        print(check_it_out)
    i=0
    while(i<5)
        i += 1
        print("i is" + str(i))


## Recursion Recap:
    def recur(i):
        if (i<5):
            print("i is " + str(i))
            recur(i + 1)
    recur(0)

This will print 0, 1, 2, 3, and 4.  Not 5 because 5 is not less than 5.


read through 16.2 in online textbook thinkcspy