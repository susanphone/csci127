Your face as data
# Dictionaries Part 3
## Key/Value Pairs
    Mutable (like lists)
    Mapping Type (unlike lists)
    {"key" : "value:}
    Key must be immutable type
    Value can be 

## Methods
    _.keys() = return the keys in the dictionary
    _.values() = return the values in the dicitonary
    _.items() = list of everything
    _get.(key) = returns the value and returns none if value does not exist.
        d.get('goat', 'No such entry')
            returns as no such entry as the otherwise when no value exists.
## Aliasing vs Copying
    mine = d
    mine
    {'ape': 'woo', 'bee': 'buzz', 'cat': 'meow', 'dog': 'bark'}
    
    yours = d.copy()
    del yours['cat']
    yours
    {'ape': 'woo', 'bee': 'buzz', 'dog': 'bark'}
    d['goat'] = 'baaa'
   
    d
    {'ape': 'woo', 'bee': 'buzz', 'cat': 'meow', 'dog': 'bark', 'goat' : 'baaa'}
   
    mine
    {'ape': 'woo', 'bee': 'buzz', 'cat': 'meow', 'dog': 'bark', 'goat' : 'baaa'}
    
    yours
    {'ape': 'woo', 'bee': 'buzz', 'dog': 'bark'}
### Copying takes a whole dict and allows you to add more to that dictionary and remain different from the original if the original were to change.
