# # year = int(input("Enter your birth year: "))
# # for i in range(year):
# #     currentYear = 2020
# #     age  = (currentYear - year)

# # print("Happy Birthday! You are " + str(age) + " years old"

# sequence1 = [2, 3, 4]
# sequence2 = [2, 4, 3]
# sequence3 = [2, 4, 8]
# def cribbage_sequence(card_list):
#     card1 = sequence1.sort()
#     card2 = sequence2.sort()
#     card3 = sequence3.sort()
#     if (sequence1[1] - sequence1[0]) is not 1:
#         return False
#     return True
#     if (sequence2[1]- sequence2[0]) is not 1:
#         return False
#     return True
#     if (sequence3[1]- sequence3[0]) is not 1:
#         return False
#     return True
    


# def main():
#     print("cribbage sequence: 2, 3, 4")
#     cribbage_sequence(sequence1)
#     print(True)
#     print("cribbage sequence: 2, 4, 3")
#     cribbage_sequence(sequence2)
#     print(True)
#     print("(cribbage sequence: 2, 4, 8")
#     cribbage_sequence(sequence3)
#     print(False)
# main()
import random
import string

length  = input("Enter the number of characters for password: ")
def generate_password(length):
    char = string.ascii_letters
    return ''.join((random.choice(char))
    for i in range(length)):
        print("Your random generated password with "+ str(length) + " characters is : ")
        print(length)
        