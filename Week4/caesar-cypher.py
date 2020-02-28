import string   #string.ascii...


def encode(m, o):
    answer = ""
    m = m.upper()
    for char in m:
        if char in string.ascii_uppercase:
            position = string.ascii_uppercase.index(char)
            position += o               #position gets position + 1
            answer += string.ascii_uppercase[position % 26] #answer gets the position index
        else:                                                   # and stick it in answer
            answer += char                  #numbers stay the same

    return answer


def main():
    message = input("input: ")
    offset = int(input("offset: "))
    encoded_message = encode(message, offset) #the answer
    print(encoded_message)      #print results


main()
