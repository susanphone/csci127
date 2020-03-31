# Dictionaries
### Key/value pairs

## Review Functions:
Step 1:

    day = input("What day is it(M, T, W, R, F, S, U)?")
    day.upper()

    if day == 'M' or day == 'W' or day == 'F':
        message = "Class meets at 9:00"
    elif day == 'R':
        message = "Lab day"
    else:
        message = "Day off!
    
    print(message)

Step 2: Identify the code to run as a function
    
    if day == 'M' or day == 'W' or day == 'F':
        message = "Class meets at 9:00"
    elif day == 'R':
        message = "Lab day"
    else:
        message = "Day off!
    print(message)
Step 3: Define the function
    
    def get_message(day):
        if day == 'M' or day == 'W' or day == 'F':
            message = "Class meets at 9:00"
        elif day == 'R':
            message = "Lab day"
        else:
            message = "Day off!
        print(message)

Step 4: Call the function
    
    get_message(day)

### Before:
    day = input("What day is it(M, T, W, R, F, S, U)?")
    day.upper()

    if day == 'M' or day == 'W' or day == 'F':
        message = "Class meets at 9:00"
    elif day == 'R':
        message = "Lab day"
    else:
        message = "Day off!
    
    print(message)

### After
    day = input("What day is it(M, T, W, R, F, S, U)?")
    day.upper()
    def get_message(day):
        if day == 'M' or day == 'W' or day == 'F':
            message = "Class meets at 9:00"
        elif day == 'R':
            message = "Lab day"
        else:
            message = "Day off!
        print(message)
    
    get_message(day)

### Argument vs Parameter(d vs day)
    day = input("What day is it(M, T, W, R, F, S, U)?")
    day.upper()
    def get_message(d):
        if d == 'M' or d == 'W' or d == 'F':
            message = "Class meets at 9:00"
        elif d == 'R':
            message = "Lab day"
        else:
            message = "Day off!
        print(message) #print could also be return
    
    get_message(day)    #but then aprint statement would have to be added to this line

## Windows vs Mac
### Files
    Mac/files
    Windows\files
### Filenames, Paths
    Mac         ls
    Windows     dir
    cd ..

## Relative Path: How to navigate files
to go up a path use ..
        CSCI127/programs/census.py
        CSCI127/files/census.txt
    file = open("../files/census.txt", "r")
    .. takes the file from programs to CSCI127
    then since you're in CSCI127 you can go to files and census.txt

## csv pre-processing
        open file in excel
            replace all , with ..
            replace all ' with ^
            replace all authors .. with/empty/
        in program file:
            file = open(input_file, encoding = "ISO-8859-1")

## Methods: 
### A function that's made to work only for a certain object.
#### object.method(parameter)
    Examples:
    my_turtle.forward(100)
    my_file.readline()
    my_string.split(',')
    my_dictionary.get(key)
