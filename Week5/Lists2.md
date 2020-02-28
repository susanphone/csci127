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
        yourlist = mylist[:]
        mylist[0] = 34
            [34, 2, 3]
        yourlist
            [5, 2, 3]
This is known as list aliasing and list cloning.

## List Methods:  This is how lists are mutable
    
### append(#element)
    Used to adding elements to the last position of a list
### insert(position, element)
    Used to insert an element in a certain position
### extend(list2)
    Adds content to list2 to the end of list1.
### sum(list)
    Used to calculate the sum of all the elements of a list.
### count(element)
    Calculates total occurrences of a given element of a list.
### length(len(list))
    Calculates the total length of a list.
### index(element[start[end,]])
    Returns the index of first occurrences. Start and end index are not necessary parameters.
### min(list)
    Calculates minimum of all the elements of a list
### max(list)
    Calculates maximum of all elements of the list.
### reverse():
    sorted([list[, key[, Reverse_Flag]]])
    list.sort([key,[Revese_flag]])
    
    Sort the given data structure in ascending order. Key and reverse_flag arenot necessary parameters and reverse_flag is set to False, if nothing is passed through sorted().
### pop([index])
    Index is not a necessary parameter, if not mentioned it takes the last index.
### del()
    Element to be deleted is mentioned using list name and index.
### remove(element)
    Element to be deleted is mentioned using list name and element.
### copy()
    Return a shallow copy of the list. Equivalent to a [:]
### dict()
    Builds dictionaries directly from sequences of key-value pairs. Can also be use to create dictionaries from arbitrary key and value expressions.
### Sort() 
    Only letters or only numbers

## Pure functions
    Creating a copy of the string

