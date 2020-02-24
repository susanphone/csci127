# Lists
        A collection of objects, where each object is identified by an index. Like other types str, int, float, etc. there is also a list type-converter function that tries to turn its argument into a list.
#### lists are created using brackets

#### you cannot concatenate a list with a string

### Lists and string:
    Both are iterable (for loop)
    Both can be concatenated
    Both can be indexed
    Check length with len()
    Lists are mutable --- like silly putty
    String are immutable

## what can you do with a list?
#### clone or alias
        Clone:
        To create a new object that has the same value as an existing object. Copying a reference to an object creates an alias but doesn’t clone the object.
         
         Alias:
        Multiple variables that contain references to the same object.
### split
        split() turns white spaces into a list.
### join
        adding the elements of a list together to create a string with delimeter
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

# Tuple
    A sequential collection of items, similar to a list. Any python object can be an element of a tuple. However, unlike a list, tuples are immutable.
        x=(1, 2, 3)
        y = x
        x =(2, 4, 6)
        y
        (1, 2,3)
    