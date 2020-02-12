# Recap Lists
    Adding Lists together
    Length
    True and False statements in a list
    Indexing in a list 
        rows[1][2]
            This is the second row and third element
    Replacement
        row_1[0] = "Molly"
            This changes the first element of row 1
    Slicing
        Deletion
            Entering [1:3] would show element 2 and 4 and ommit 1 and 3.
        Insert
            Enter position and element. Does not overwrite
                insert(1, 'Anna')
        Append VS. Concatenation
            Appending is adding something on
            Concatenating is adding an element but it stays separate.
        Count
            Number a times an element appears in the list
    Indexing
        What position an element is located.
    Traversal
        Go through every item in a for loop and go through the function. 
        Example: Iterate through the number of items in a list
    Pure Function
        Does not modify its parameters. No side effects.

# Split
        split() turns white spaces into a list.
            "For score and seven years"
            ["For", "score", "and", "seven", "years"]
            split("and")
            ["For score", "seven years"]
# Join

        " ".join(speech)
        "For score and seven years"
        "+++".join(speech)
        "For+++score+++and+++seven+++years"
# Tuple
    Is not mutable
        x=(1, 2, 3)
        y = x
        x =(2, 4, 6)
        y
        (1, 2,3)