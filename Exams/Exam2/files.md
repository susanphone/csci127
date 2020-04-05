# Files

### Opening a file:
    To read a file:
        open(filename, "r")
    To write to a file:
        open(filename, "w")
    To close a file: 
        filevariable.close()

### How to use files within programs:
    open file giving it a variable.
    use variable and manipulate the file
    move new data to new list
    close the file

    files and program must be located in the same folder in order for programs to find the file.
#### example:
    census_file = open("census.txt", "r")
    for one_line in census_file:
        values = one_line.split()
        print("State: " + values[0] + ", Population: " + values[1])
        census_file.close()

    f = open("studentdata.txt", "r")
    for aline in f:
        items = aline.split()
        if len(items[1:])>6:
            print(items[0])
    f.close()

### CSV: Comma Separated Values
    using spreadsheets to create programs:
        Program 3
        Magnitude Lab

