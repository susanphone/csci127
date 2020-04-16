import numpy as np
import random

# -------------------------------------------------
# CSCI 127, Lab 9
# April 2, 2020
# Susan McCartney
# -------------------------------------------------
# Yahtzee is used for this program, but with a twist,
# the use of eight-sided dice! 
# Since I use Linux, I noticed that the number outcomes
# might look differently to my computer than they do on
# a Windows or Mac computer.

class Die:

    def __init__(self, sides):
        """A constructor method to create a die"""
        self.sides = sides

    def roll(self):
        """A general method to roll the die"""
        return random.randint(1, self.sides)

# -------------------------------------------------


class Yahtzee:

    def __init__(self, sides):
        """A constructor method that can record 5 dice rolls"""
        self.rolls = np.zeros(5, dtype=np.int16)
        self.sides = sides

    def roll_dice(self):
        """A general method that rolls 5 dice"""
        for i in range(len(self.rolls)):
            self.rolls[i] = Die(self.sides).roll()

    def count_outcomes(self):
        """A helper method that determines how many 1s, 2s, etc. were rolled"""
        counts = np.zeros(self.sides + 1, dtype=np.int16)
        for roll in self.rolls:
            counts[roll] += 1
        return counts
        
    def is_it_low_roll(self):
        """If dice rolls only 1s and/or 2s, then it is a low roll"""
        counts = self.count_outcomes()
        if (counts[1] + counts[2] == 5):
            return True
        return False

        
    def is_it_three_of_a_kind(self):
        """If the dice rolls the same number exactly three times, then it is a three of a kind"""
        counts = self.count_outcomes()
        for i in counts:
            if counts[i] == 3:
                print(counts)
                return True
        return False

    
    def is_it_large_straight(self):
        """If the 5 rolls are consecutive and each roll has a difference of 1, then it is a large straight."""
        rolls = np.sort(self.rolls)
        for i in range(4):
            if (rolls[i+1] - rolls[i]) != 1:
                return False
        return True

# -------------------------------------------------


def main(how_many):

    low_rolls = 0
    three_of_a_kinds = 0
    large_straights = 0
    game = Yahtzee(8)       # 8-sided dice

    for i in range(how_many):
        game.roll_dice()
        if game.is_it_low_roll():
            low_rolls += 1
        elif game.is_it_three_of_a_kind():
            three_of_a_kinds += 1
        elif game.is_it_large_straight():
            large_straights += 1

    print("Number of Rolls:", how_many)
    print("---------------------")
    print("Number of Low Rolls:", low_rolls)
    print("Percent:", "{:.2f}%\n".format(low_rolls * 100 / how_many))
    print("Number of Three of a Kinds:", three_of_a_kinds)
    print("Percent:", "{:.2f}%\n".format(three_of_a_kinds * 100 / how_many))
    print("Number of Large Straights:", large_straights)
    print("Percent:", "{:.2f}%".format(large_straights * 100 / how_many))

# -------------------------------------------------


main(20000)
