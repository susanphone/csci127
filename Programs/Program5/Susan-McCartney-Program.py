import numpy as np
import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 5: Peg Rectangle Solitaire    |
# Susan McCartney                       |
# Last Modified: April 20, 2019         |
# ---------------------------------------
# Peg Solitaire using object oriented 
#programming and numpy in a game. The
#least remaining pegs, the better!
# ---------------------------------------

# ---------------------------------------
# Start of PegRectangleSolitaire Class  |
# ---------------------------------------

class PegRectangleSolitaire:

    def __init__(self, rows, columns, empty_row, empty_col):
        self.board = np.full((rows, columns), True)
        self.board[empty_row][empty_col] = False
        self.pegs_left = rows * columns - 1
        
# ---------------------------------------

    def __str__(self):
        answer = "   "
        for column in range(self.board.shape[1]):
            answer += " " + str(column + 1) + "  "
        answer += "\n"
        answer += self.separator()
        for row in range(self.board.shape[0]):
            answer += str(row + 1) + " |"
            for col in range(self.board.shape[1]):
                if self.board[row][col]:
                    answer += " * |"
                else:
                    answer += "   |"
            answer += "\n"
            answer += self.separator()
        return answer
    
# ---------------------------------------

    def separator(self):
        answer = "  +"
        for _ in range(self.board.shape[1]):
            answer += "---+"
        answer += "\n"
        return answer

# ---------------------------------------
# The four missing methods go here.  Do |
# not modify anything else.             |
# --------------------------------------|
    def game_won(self):
        if self.pegs_left <= 7:
            self.game_won = True
        return self.game_won

    def final_message(self,):
#For when the game is over if statements for
#number of remaining pegs:
        if self.pegs_left <= 2:
            self.final_message = "You're a DigiPeg Genius!"
        if self.pegs_left > 2 or self.pegs_left <= 4:
            self.final_message = "Not too shabby, rookie."
        if self.pegs_left > 4 or self.pegs_left <= 6:
            self.final_message = "That's nothing to write home about."
        if self.pegs_left >7:
            self.final_message = "You're a DigiPeg Igno-Ra-Moose"
        return self.final_message

    def legal_move(self, empty_row, empty_col): #boolean
#(row_start and end, and column_start and end)
        if self.legal_move is True:
#if peg is one away from empty space:
#if peg moved is in same column or row as empty space
    #legal move
            return self.legal_move

    def make_move(self, empty_row, empty_col):
        #init???
#(row_start and end, and column_start and end)
#if move is legal, move peg to end_row, end_column
        return self.make_move

# ---------------------------------------
# End of PegRectangleSolitaire Class    |
# ---------------------------------------

def get_choice(low, high, message):
    message += " [" + str(low) + " - " + str(high) + "]: "
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

def main():
    print("Welcome to Peg Rectangle Solitaire!")
    print("-----------------------------------\n")
    
    rows = get_choice(1, 9, "Enter the number of rows")
    columns = get_choice(1, 9, "Enter the number of columns")
    row = get_choice(1, rows, "Enter the empty space row") - 1
    column = get_choice(1, columns, "Enter empty space column") - 1   
    game = PegRectangleSolitaire(rows, columns, row, column)
    print()

    keep_going = "yes"
    print(game)
    while (not game.game_won() and keep_going.lower() == "yes"):
        row_start = get_choice(1, rows, "Enter the row of the peg to move") - 1
        col_start = get_choice(1, columns, "Enter the column of the peg to move") - 1
        row_end = get_choice(1, rows, "Enter the row where the peg lands") - 1
        col_end = get_choice(1, columns, "Enter the column where the peg lands") - 1
        if game.legal_move(row_start, col_start, row_end, col_end):
            game.make_move(row_start, col_start, row_end, col_end)
        else:
            print("Sorry.  That move is now allowed.")
        print()
        print(game)
        if not game.game_won():
            keep_going = input("Do you want to continue (yes or no): ")

    game.final_message()

# ---------------------------------------

main()
