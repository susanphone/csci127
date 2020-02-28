# Question 1: Input Birth Year
    birthyear = input("enter birthyear: ")
    age = 2020 - int(birth_year)
    print("Happy Birthday, you are ", age, "years old!")

# Question 2: Cribbage Sequence
### use straight from program 2

    def cribbage_squence(card_list):
        card_list.sort()
        if (card_list[0] + 1 == card_list[1] and card_list[1] + 1 == card_list[2]):
            return True
        else:
            return False  
                                #uninary statement would return none
    print(cribbage_sequence([2, 3, 4]))
    print(cribbage_sequence([2, 4, 3]))
    print(cribbage_sequence([2, 4, 8]))

    >>> True
        True
        False

# Question 3: Password Generator
    import random
    import string           #use of ascii

    def generate_password(length):
        password = ""
        #password = string.ascii_letters
        for i in range(length):
            password += string.ascii_letters[random.randint(0, 51)] #0 is one
        return password  


    print(generate_password(5)) #length of password