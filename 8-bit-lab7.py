# --------------------------------------
# CSCI 127, Lab 7                      |
# March 5, 2020                        |
# Susan McCartney                      |
# --------------------------------------
# This program takes a csv file, splits|
# the contents of the file into a list |
# and use a dictionary to represent a  |
# key and corresponding value. Using a |
# sentence written in the main         |
# function, the program will output a  |
# character and it's corresponding     |
# 8-bit.                               |
# --------------------------------------

# NOTE: Using excel spreadsheet removes any starting zeros unless zero values are activated in the excel spreadsheet program. Using text editor makes the program work properly. :)


# Comma, quote, and space characters are treated differently in the ascii-codes csv because within the csv they are identified as "comma", "quote", and "space" and in order to get them to be their actual characters you have to change the character in the file using an if statement when a comma, quote, or space appear in the sentence.


# create_dictionary function returns a dictionary where the keys are characters and the values are the 8-bit representations.
def create_dictionary(file_name):
    file = open(file_name, "r")
    char_to_bit = {}

    for line in file:
        file_list = line.split(',')

        key = file_list[1]
        value = file_list[0]

        key = key.strip()

        if key == "comma":
            key = ","
        if key == "space":
            key = " "
        if key == "quote":
            key = "'"

        char_to_bit[key] = value

    file.close()
    
    return char_to_bit


# The translate function uses three parameters- sentence, dictionary, and filename - to take the dictionary and get the 8-bit from the corresponding character. If the value does not exist for a character, the value for that character will print "UNDEFINED" where the 8-bit value would go.
def translate(sentence, dictionary, file_name):
    for char in sentence:
        value = dictionary.get(char)
        if value is None:
            print("UNDEFINED     " + char)
        else:
            print(value + "      " + char)
    # --------------------------------------


def main():
    dictionary = create_dictionary("ascii-codes.csv")
    sentence = "A long time ago in a galaxy far, far away..."
    translate(sentence, dictionary, "output-1.txt")
    sentence = "Montana State University (406) 994-0211"
    translate(sentence, dictionary, "output-2.txt")
    sentence = "“True friends stab you in the front.” —Wilde"
    translate(sentence, dictionary, "output-3.txt")
# --------------------------------------


main()
