# -----------------------------------------+
# Susan McCartney and Isabell Erickson     |
# CSCI 127, Program 2                      |
# Last Updated: February 10, 2020          |
# -----------------------------------------|
# Simplified Poker Hand evaluation system. |
# -----------------------------------------+


def get_all_ranks(hand):
    result = []
    for card in hand:
        result.append(card[0])
    return result


#royal flush contains one suit and thevalue of the cards are ten and above.
def royal_flush(hand):
    for i in range(len(hand)):
        if i < len(hand)-1 and hand[i][1] is not hand[i+1][1]:
            return False
        if hand[i][0] < 10:
            return False
    return True

def straight_flush(hand):
   #if hand contains five consecutive cards of the same suit  
    for i in range(len(hand)):
        if i < len(hand)-1 and hand[i][1] is not hand[i+1][1]:
            return False
        if i is 0:
            continue
        if (hand[i][0] - hand[i-1][0]) is not 1:
            return False
    return True

def straight(hand):
    #if hand contain five consecutive cards irrespective of suit
    for i in range(len(hand)):
        if i is 0:
            continue
        if (hand[i][0] - hand[i-1][0]) is not 1:
            return False
    return True


def four_of_a_kind(ranks):
    numbers  = []
    for card in ranks:
        ranks.append([row[0] for row in numbers])

        # if (numbers[0]-numbers[2]) or (numbers[2] - numbers[4]) is 0:
        #     if (numbers[0]-numbers[1]) or (numbers[3] - numbers[4]) is 0:
        #         return True
        # else:
        #     return False

def full_house(ranks):
    for card in ranks:
        if (ranks[0]-ranks[2]) or (ranks[2] - ranks[4]) is not 0:
            if (ranks[0]-ranks[1]) or (ranks[3] - ranks[4]) is not 0:
                return False
        return True

# def three_of_a_kind(ranks):
#     for card in ranks:
#         if (ranks[0]-ranks[2]) or (ranks[2] - ranks[4]) or (ransk[1]- rank[3]) is 0:
#             return True
#         else: 
#             return False

# def two_pair(ranks):
#     #if hand contain two sets of two cards of the same
#     return False

# def one_pair(ranks):
#     #if hand contains two cards that are the same
#     return False


# -----------------------------------------+
# Do not modify the evaluate function.     |
# -----------------------------------------+

#Dont touch evaluate function
def evaluate(poker_hand):
    poker_hand.sort()
    poker_hand_ranks = get_all_ranks(poker_hand)
    
    print(poker_hand, "--> ", end="")
    if royal_flush(poker_hand):
        print("Royal Flush")
    elif straight_flush(poker_hand):
        print("Straight Flush")
    elif four_of_a_kind(poker_hand_ranks):
        print("Four of a Kind")
    elif full_house(poker_hand_ranks):
        print("Full House")
    elif straight(poker_hand):
        print("Straight")
    # elif three_of_a_kind(poker_hand_ranks):
    #     print("Three of a Kind")
    # elif two_pair(poker_hand_ranks):
    #     print("Two Pair")
    # elif one_pair(poker_hand_ranks):
    #     print("One Pair")
    else:
        print("Nothing")
		
# -----------------------------------------+
 #Test data
def main():
    print("CSCI 127: Poker Hand Evaluation Program")
    print("---------------------------------------")
    evaluate([[10, "spades"], [14, "spades"], [12, "spades"], [13, "spades"], [11, "spades"]])  # royal flush
    evaluate([[10, "clubs"], [9, "clubs"], [6, "clubs"], [7, "clubs"], [8, "clubs"]])           # straight flush
    evaluate([[2, "diamonds"], [7, "clubs"], [2, "hearts"], [2, "clubs"], [2, "spades"]])       # 4 of a kind
    evaluate([[8, "diamonds"], [7, "clubs"], [8, "hearts"], [8, "clubs"], [7, "spades"]])       # full house
    evaluate([[13, "diamonds"], [7, "clubs"], [7, "hearts"], [8, "clubs"], [7, "spades"]])      # 3 of a kind
    evaluate([[10, "clubs"], [9, "clubs"], [6, "clubs"], [7, "clubs"], [8, "spades"]])          # straight
    evaluate([[10, "spades"], [9, "clubs"], [6, "diamonds"], [9, "diamonds"], [6, "hearts"]])   # 2 pair
    evaluate([[10, "spades"], [12, "clubs"], [6, "diamonds"], [9, "diamonds"], [12, "hearts"]]) # 1 pair
    evaluate([[2, "spades"], [7, "clubs"], [8, "diamonds"], [13, "diamonds"], [11, "hearts"]])  # nothing

# -----------------------------------------+

main()
