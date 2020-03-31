# NumPy
## Arrays
    a common data structure 
    a bank of memory addresses 
    each address gets a cell
        within each cell you can store letters or numbers
        you can also store a list within the cell
        each cell is a certain number of bytes.
    the index starts at zero to make it easy to find the array via index
    a reference is suppose to all be the same size.
### ndarray: any number demension array
### NumPy is written in compiled C
### Install numpy in terminal
#### open demo.py
    import numpy as np mean use numpy in the program by typing "np"
    inport math
    How to find the mean
    How to find the standard deviation
    second way to get the mean
        print(shoulder_heights.mean())
        print(shoulder_heights.std())
        shoulder_heights.sort()
        print(shoulder_heights)
    many methods available for numpy array if you search numpy array
#### open tutorial1.py
    broadcasting helps to avoid using forloops
    b2 = np.array(['a', 'b', 'c', 'd'])
        array(['abcdefghij', 'b', 'c', 'd'], dtype='<U10')
### arange
    return evenly spaced values within a given value
    [star, stop, step]
### reshape
    return element in rows and columns
    (4,10) is four rows and 10 columns. 
    If this is not even, you will get an error. 
    Therefore, arange and reshape have to work togethe and match up.



