# Dictionaries - according to the textbook
So far - strings, lists, and tuples - are squential collections ordered from left to right and use integers as indices to access the values the contain. Meaning indexing the collection to get the value.
## A dictionary is a map. A map is an unordered associative collection. Mapping happens but using a key, which are immutable, and the key is attached to a value or data object.

## To start a dictionary:
### Start with an empty dictonary denoted as {}
#### From there you can add key-value pairs
Here is a english to spanish dictionary:

    end2sp = {}
    eng2sp['one'] = 'uno'
    eng2sp['two'] = 'dos'
    eng2sp['three'] = 'tres'

## Using existing dictionary:
dict = {key: value, key2:value2}
### key-value pairs are separated by commas. Each pair contains a key and value separated by a colon.

## What to do with dictionaries
### Delete: (del) removes a key-value pair from a dictionary
    inventory = {'apples' : 430, 'bananas' : 312, 'oranges' : 525, 'pears' :217}
    del inventory['pears']
    inventory = ['apples': 430, 'bananas': 312, 'oranges' : 525]

### Reassign a new value to a key
#### take away value
    inventory = {'apples' : 430, 'bananas' : 312, 'oranges' : 525, 'pears' :217}
    inventory['pears'] = 0

    inventory = ['apples': 430, 'bananas': 312, 'oranges' : 525, 'pears' : 0]
#### or add value
    inventory = {'apples' : 430, 'bananas' : 312, 'oranges' : 525, 'pears' :217}
    inventory['bananas'] = inventory['bananas'] + 200

    numItems = len(inventory)
    
    inventory = ['apples': 430, 'bananas': 512, 'oranges' : 525, 'pears': 217]

## Dictionary methods:
    Method          Parameters          Description
    keys                none                Returns a view of the keys in the dict
    values              none                Returns a view of the values in the dict
    items               none                Returns a view of the key-value pairs in the dict
    get                 key                 Returns the value associated with key; None otherwise
    get                 key,alt             Returns the value associated with key; alt otherwise

### Keys Method
#### Method 1:
    inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

    for akey in inventory.keys(): 
    print("Got key", akey, "which maps to value", inventory[akey])

    ks = list(inventory.keys())
    print(ks)
Outcome would look like this:

    Got key apples which maps to value 430
    Got key bananas which maps to value 312
    Got key oranges which maps to value 525
    Got key pears which maps to value 217
    ['apples', 'bananas', 'oranges', 'pears']
#### Method 2: use a for loop
    inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

    for k in inventory:
        print("Got key", k)

The outcome would look like this:

    Got key apples
    Got key bananas
    Got key oranges
    Got key pears

## Dot Notation(Object.Method(Parameter))
Dictionary methods use dot notation, which specifies the name of the method to the right of the dot and the name of the object on which to apply the method immediately to the left of the dot. The empty parentheses in the case of keys indicate that this method takes no parameters.

## Value and Item Method:
These return view objects, which can be turned into lists ir iterated over directly. 

    inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

    print(list(inventory.values()))
    print(list(inventory.items()))

    for (k,v) in inventory.items():
        print("Got", k, "that maps to", v)

    for k in inventory:
        print("Got", k, "that maps to", inventory[k])
This outcome would look like this:

    [430, 312, 525, 217]
    [('apples', 430), ('bananas', 312), ('oranges', 525), ('pears', 217)]
    Got apples that maps to 430
    Got bananas that maps to 312
    Got oranges that maps to 525
    Got pears that maps to 217
    Got apples that maps to 430
    Got bananas that maps to 312
    Got oranges that maps to 525
    Got pears that maps to 217
## in and not it operators: 
### Test if a key is in the dict and prevent a non-existent runtime error from occuring.
    inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
    print('apples' in inventory)
    print('cherries' in inventory)

    if 'bananas' in inventory:
        print(inventory['bananas'])
    else:
        print("We have no bananas")
The outcome would look like this:
    
    True
    False
    312

## Get Method:
### The get method allows us to access the value associated with a key, but it will not cause a runtime error if the key is not present. It will instead return None.
There exists a variation of get that allows a second parameter that serves as an alternative return value in the case where the key is not present.

    inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

    print(inventory.get("apples"))
    print(inventory.get("cherries"))

    print(inventory.get("cherries", 0))

This outcome will look like this:

    430
    None
    0

## Aliasing and Copying:
### Dictionaries are mutable, so...
### whenever two variables refer to the same dictionary object, changes to one variable affect the other variable as well.

    opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
    alias = opposites

    print(alias is opposites)

    alias['right'] = 'left'
    print(opposites['right'])
The outcome would look like this:

    True
    left
## Copy Method:
A way to modify a dictionary while keeping a copy of the original dictionary.

    acopy = opposites.copy()
    ['right'] = 'left'    # does not change opposites
## Matrix:
A matrix is a two dimensional collection, typically thought of as having rows and columns of data.
## Sparsed Matrices:
A matrix that has very few values that are nonzero. There is no reason to store very little zeros.

    matrix = [[0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 3, 0]]
    Using a list of lists representation, we will have a list of five items, each of which is a list of five items. The outer items represent the rows and the items in the nested lists represent the data in each column.

### A sparse matrix can be used in a dictionary. For the keys we can use tuples that contain the row and column numbers.
    matrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}

We only need three key-value pairs, one for each nonzero element of the matrix. Each key is a tuple, and each value is an integer
### Alternative get method for matrices
    matrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}
    print(matrix.get((0,3)))

    print(matrix.get((1, 3), 0))

The outcome is:

        1
        0

# Glossary
## Dictionary
        A collection of key-value pairs that maps from keys to values. The keys can be any immutable type, and the values can be any type.
## Key
        A data item that is mapped to a value in a dictionary. Keys are used to look up values in a dictionary.
## Key-Value Pair
        One of the pairs of items in a dictionary. Values are looked up in a dictionary by key.
## Mapping-Type
        A mapping type is a data type comprised of a collection of keys and associated values. Python’s only built-in mapping type is the dictionary. Dictionaries implement the associative array abstract data type.
