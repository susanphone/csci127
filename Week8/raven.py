import string

# ---------------------------
#makes a long line of lowercase letters. 
#No special characters, numbers or new lines.

def count_letters(text):
    table = {}
    for letter in text:
        if letter not in table:
            table[letter] = 1
        else:
            table[letter] = table[letter] + 1
    return table
            
def keep_letters(filename):
    file = open(filename, "r")
    modified_text = ""

    for line in file:
        line = line.lower()
        for letter in line:
            if letter in string.ascii_lowercase:
                modified_text += letter

    file.close()
    return modified_text

# ---------------------------


text = keep_letters("raven.txt")
# print(text)


poe = count_letters(text)
print(poe)