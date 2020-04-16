# -----------------------------------------+
# Susan McCartney                          |
# CSCI 127, Lab 4                          |
# February 13, 2020                        |
# -----------------------------------------|
# A program that prompts a list of words and|
# then a function is used to output those  |
# words and their frequencies.             |
# -----------------------------------------+

# count_frequencies counts frequencies of the occurences of multple words in a sentence.
def count_frequencies(wordlist):
    counts = dict()
    for eachWord in wordlist:
        if eachWord in counts:
            counts[eachWord] += 1
        else:
            counts[eachWord] = 1
    return counts


def main():
    sentence = input("Please enter a sentence: ")
    punctuation = ['!', '.', ',', ':', ';', '%','$', '(', ')', '~', '`', '[', ']', '-', '/', '<', '>', '^', "*", '?']

    for char in sentence:
        if char in punctuation:
            #replaces sentence with a update sentence without punctuation.
            #Words that have contractions will still keep their apostrophes
            sentence = sentence.replace(char, "")
    
    # key-word and value-number of occurances
    listOfWords = sentence.lower().strip().split(" ")
    wordFrequencyCount = count_frequencies(listOfWords)
    for key, value in wordFrequencyCount.items():
        print(key, value)

main()
