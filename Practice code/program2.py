hand = [[10, "spades"], [10, "hearts"], [10, "clubs"], [10, "diamonds"], [3, "hearts"]]
hand.sort()
# print(hand)
value = []
numbers = []
value.append([row[0] for row in hand])
numbers = (value[0])
if (numbers[0]-numbers[2]) or (numbers[2] - numbers[4]) is 0:
    if (numbers[0]-numbers[1]) or (numbers[3] - numbers[4]) is 0:
        print(numbers)



