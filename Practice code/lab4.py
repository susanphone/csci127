import string
def main():
    def count_frequencies(wordlist):
        sentence = input("Please enter a sentence: ")

punctuation = ['!', '.', ',', ':', ';', '%', '$', '(', ')', '~', '`', '[', ']', '-']
sentence = input("Please enter a sentence: ")
#key-word and value-number of occurances
for char in sentence:
    if char in punctuation:
        # sentence.replace(char, "")
        sentence = sentence.replace(char, "")
counts = dict()   
words = sentence.lower().split(" ")
for newWords in words:
    if newWords in counts:
        counts[newWords] += 1
    else:
        counts[newWords] = 1
for key, value in counts.items():
    print(key, value)

