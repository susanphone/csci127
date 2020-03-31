c = 'cat'
d = 'dog'
a = 'ape'
b = 'bee'
#variables that reference a string

animals = [a, b, c, d]
print(animals)
sounds = ['woo', 'buzz', 'meow', 'bark']
print(sounds)
for i in range(4):
    print(i)
#build a dictionary
d ={}
for i in range(4):
    #make a key and a value
    key = animals[i] #list of animals
    value = sounds[i] #list of sounds
    d[key] = value
    print(d)
    #d[animals[i]]=sounds[i] one line instead of three
    