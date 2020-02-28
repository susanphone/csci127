# -------------------------------------------
# CSCI 127, Lab 3                           |
# February 06, 2020                         |
# Susan McCartney                           |
# -------------------------------------------
# Calculate how many bilabial consonenents  |
# are in a sentence using three techniques. |
# -------------------------------------------

def count_built_in(sentence):
    totalCount = sentence.count("b")
    totalCount += sentence.count("m")
    totalCount += sentence.count("p")
    return totalCount


sentence = "bees?"
def count_iterative(sentence):
    bilabial = ["b", "m", "p"]
    totalCount = 0
    for char in sentence:
        if char in bilabial:
            totalCount += 1 
    return totalCount       #bilabials should be adding together


def count_recursive(sentence):      #function that takes an argument
        totalCount = 0
        bilabial = ["b", "m", "p"]
        if len(sentence) > 1:
            totalCount += count_recursive(sentence[0:len(sentence)-1])
            totalCount += count_recursive(sentence[(len(sentence) - 1)])
            return totalCount
        else:
            if sentence in bilabial:
                return 1
            else:
                return 0


#--------------------------------------


def main():
    answer = "yes"
    while (answer == "yes") or (answer == "y"):
        sentence = input("Please enter a sentence: ")
        sentence = sentence.lower()
        print()
        print("Counting bilabial consonents  using ...")
        print("---------------------------------------")
        print("Built-in function =", count_built_in(sentence))
        print("Iteration =", count_iterative(sentence))
        print("Recursion =", count_recursive(sentence))
        print()
        answer = input("Would you like to continue: ").lower()
        print()

#--------------------------------------


main()
