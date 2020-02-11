# Lists:
### Lists and Strings:
        Both are iterable (for loop)
        Both can be concatenated
            But you cannot concatenate a string and list together
        Both can be indexed
        Check length with len()
Slice is done like so:  [start:end]

#### the difference:
    Lists are mutable --- like silly putty
    String are immutable
## How to copy a list without retyping it:
        mylist = [1, 2, 3]
        yourlist = mylist
        mylist[0] = 5
        mylist
            [5, 2, 3]
        yourlist
            [5, 2, 3]
    Why did this occur?
        yourlist and mylist have the same value.
    How to split in a split: [4][1]
            This would give the value within the list.
    Try slicing the whole list to copy it.
        youlist = mylist[:]
        mylist[0] = 34
            [34, 2, 3]
        yourlist
            [5, 2, 3]
This is known as list aliasing and list cloning.

### List Methods:  This is how lists are mutable
        Sort() Only letters or only numbers
        Reverse()
        Remove(item)
        append(item)
        count(item)

    Found in the online textbook reading

## Pure functions
    Creating a copy of the string

