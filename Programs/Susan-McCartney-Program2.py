# -----------------------------------------+
# Susan McCartney and Isabell Erickson     |
# CSCI 127, Program 2                      |
# Last Updated: February 21, 2020          |
# -----------------------------------------|
# Simplified Poker Hand evaluation system. |
# -----------------------------------------+


def get_all_ranks(hand):
    result = []
    for card in hand:
        result.append(card[0])
    return result


# royal flush contains one suit and the value of the cards are ten and above.
# check for one suit then check to value of cards to be 10 or over.
def royal_flush(hand):
    for i in range(len(hand)):
        if i < len(hand)-1 and hand[i][1] is not hand[i+1][1]:
            return False
        if hand[i][0] < 10:
            return False
    return True


# straight flush  hand contains five consecutive cards of the same suit.
# check for one suit, then check that the difference between each card is 1.
def straight_flush(hand):
    for i in range(len(hand)):
        if i < len(hand)-1 and hand[i][1] is not hand[i+1][1]:
            return False
        if i is 0:
            continue
        if (hand[i][0] - hand[i-1][0]) is not 1:
            return False
    return True


# if hand contain five consecutive cards irrespective of suit.
# check that the difference of value between each card is 1.
def straight(hand):
    for i in range(len(hand)):
        if i is 0:
            continue
        if (hand[i][0] - hand[i-1][0]) is not 1:
            return False
    return True

# four of a kind is four cards that are the same value.
# it compares first and second cards, and second and third,
# and third and fourth in a loop;
# if they are equal, they are added to "four"
# if there is a four, then it is four of a kind.
def four_of_a_kind(ranks):
    four = 0
    for i in range(len(ranks) - 3):
        if ranks[i] == ranks[i+1] and ranks[i+1] == ranks[i+2] and ranks[i+2] == ranks[i+3]:
            four += 1
    if four == 1:
        return True


# full house hand contains three of a kind and two of a kind.
# if the first card and third card are the same OR
# if the second card and the fifth card are the same
# then there are three of a kind.
# if the first and second card are the same OR
# if the fourth or fifth card are the same
# then there is a pair.
# if there is three of a kind and a pair then it is a full house.
def full_house(ranks):
    for card in ranks:
        if (ranks[0]-ranks[2]) is not 0 or (ranks[2] - ranks[4]) is not 0:
            if (ranks[0]-ranks[1]) is not 0 or (ranks[3] - ranks[4]) is not 0:
                return False
        return True


# three of a kind hand contains three cards with the same value, and two unique values.
# compares first and second cards, and second and third cards in a loop; if they are equal,they are added to "three"
# if there is a three, then it is three of a kind.
def three_of_a_kind(ranks):
    three = 0
    for i in range(len(ranks) - 2):
        if ranks[i] == ranks[i+1] and ranks[i+1] == ranks[i+2]:
            three += 1
    if three == 1:
        return True


# two pair is when two sets of two cards are the same rank.
# compares two cards at a time in a loop; if two are the same rank, they are incremented "pairs"
# if there are two pairs, then it is two pair.
def two_pair(ranks):
    pairs = 0
    for i in range(len(ranks) - 1):
        if ranks[i] == ranks[i+1]:
            pairs = pairs + 1
    if pairs == 2:
        return True


# one pair is where there are four unique values and two cards are the same.
# compares two cards at a time in a loop; if two are the same, they are added to "pairs";
# if there is one pair, then it is a pair.
def one_pair(ranks):
    pairs = 0
    for i in range(len(ranks) - 1):
        if ranks[i] == ranks[i+1]:
            pairs = pairs + 1
    if pairs == 1:
        return True

# -----------------------------------------+
# Do not modify the evaluate function.     |
# -----------------------------------------+


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
    elif three_of_a_kind(poker_hand_ranks):
        print("Three of a Kind")
    elif two_pair(poker_hand_ranks):
        print("Two Pair")
    elif one_pair(poker_hand_ranks):
        print("One Pair")
    else:
        print("Nothing")

# -----------------------------------------+


def main():
    print("CSCI 127: Poker Hand Evaluation Program")
    print("---------------------------------------")
    evaluate([[10, "spades"], [14, "spades"], [12, "spades"],
              [13, "spades"], [11, "spades"]])  # royal flush
    evaluate([[10, "clubs"], [9, "clubs"], [6, "clubs"], [
             7, "clubs"], [8, "clubs"]])           # straight flush
    evaluate([[2, "diamonds"], [7, "clubs"], [2, "hearts"], [
             2, "clubs"], [2, "spades"]])       # 4 of a kind
    evaluate([[8, "diamonds"], [7, "clubs"], [8, "hearts"], [
             8, "clubs"], [7, "spades"]])       # full house
    evaluate([[13, "diamonds"], [7, "clubs"], [7, "hearts"],
              [8, "clubs"], [7, "spades"]])      # 3 of a kind
    evaluate([[10, "clubs"], [9, "clubs"], [6, "clubs"], [
             7, "clubs"], [8, "spades"]])          # straight
    evaluate([[10, "spades"], [9, "clubs"], [6, "diamonds"],
              [9, "diamonds"], [6, "hearts"]])   # 2 pair
    evaluate([[10, "spades"], [12, "clubs"], [6, "diamonds"],
              [9, "diamonds"], [12, "hearts"]])  # 1 pair
    evaluate([[2, "spades"], [7, "clubs"], [8, "diamonds"],
              [13, "diamonds"], [11, "hearts"]])  # nothing

# -----------------------------------------+


main()
