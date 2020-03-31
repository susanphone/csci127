import string

# --------------------------------

#change all words to lowercase and removes punctuation and digits.
def sentence_to_words(sentence):
    sentence = sentence.lower()
    reduced_sentence = ""
    for character in sentence:
        if character in string.ascii_lowercase or character == " ":
            reduced_sentence += character
    return reduced_sentence

# --------------------------------

# takes each string in the list and makes the word the key and returns the count value of the word or returns zero.
def update(dictionary, words):
    for word in words:
        dictionary[word] = dictionary.get(word, 0) + 1

# --------------------------------

# find a way to print the most frequently occuring word. 
# use a for loop and compare the count of each word.
def most_frequent(dictionary):
    # print("Print the most frequently occuring word, as well as its frequency")
    word = ""
    most = 0
    for k in dictionary:    #k = key
        if most < dictionary[k]:
            most = dictionary[k]
            word = k
    print("Most common word... " + word + " : occurs " + str(dictionary[word]) + " times")
    

# --------------------------------

# START READING HERE!   
# what are the data types?
#call sentence_to_words and send the sentence from user input. Words is the return value of that function.
#update is a function taking dictionary and words and returning the value count of each word.
#while loop will only keep going unless it gets the answer no or n from user input.
def main():
    proceed = "yes"
    word_dictionary = {}
    while proceed == "yes" or proceed == "y":
        sentence = input("Please enter a sentence: ")
        words = sentence_to_words(sentence)
        word_list = words.split()
        update(word_dictionary, word_list)
        print(word_dictionary)
        most_frequent(word_dictionary)
        proceed = input("Would you like to continue? ")
        proceed = proceed.lower()

# --------------------------------


main()
