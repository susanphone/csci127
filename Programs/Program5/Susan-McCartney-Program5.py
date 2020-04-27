import numpy as np
import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 5: Peg Rectangle Solitaire    |
# Susan McCartney                       |
# Last Modified: April 24, 2020         |
# ---------------------------------------
# Peg Solitaire using object oriented
# programming and numpy in a game. The
# least remaining pegs, the better!
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
                    answer += " o |"
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

    def game_over(self):
        board_height = len(self.board)
        board_width = len(self.board[0])

        # Iterate through all board positions
        for i in range(board_height):
            for j in range(board_width):
                # Check for horizontal RtoL move
                if (j + 2) <= (board_width-1):
                    if self.legal_move(i, j, i, j + 2):
                        return False
                # Check for horizontal LtoR move
                if (j - 2) >= 0:
                    if self.legal_move(i, j, i, j - 2):
                        return False      
                # Check for vertical UtoD move
                if (i + 2) <= (board_height-1):
                    if self.legal_move(i, j, i + 2, j):
                        return False
                # Check for vertical DtoU move
                if (i - 2) >= 0:
                    if self.legal_move(i, j, i - 2, j):
                        return False
        return True



    def legal_move(self, row_start, col_start, row_end, col_end):  # boolean
        # no start peg
        if self.board[row_start][col_start] == False:
            return False
        
        # peg already exists at end spot
        if self.board[row_end][col_end] == True:
            return False
        
        is_horizontal = row_start == row_end
        is_vertical = col_start == col_end
        
        # not moving a peg or moving diagonally
        if (is_horizontal and is_vertical) or (not is_horizontal and not is_vertical):
            return False
        
        # jumping left to right over no peg
        if is_horizontal:
            is_left_to_right = col_start < col_end

            # right to left over no peg
            if not is_left_to_right and self.board[row_end][col_end+1] == False:
                return False            
            # left to right over no peg
            if is_left_to_right and self.board[row_end][col_end-1] == False:
                return False
            # not over one peg
            if abs(col_end - col_start) != 2:
                return False

        if is_vertical:
            is_up_to_down =  row_start < row_end

            # down to up over no peg
            if not is_up_to_down and self.board[row_start-1][col_end] == False:
                return False
            # up to down over no peg
            if is_up_to_down and self.board[row_end-1][col_end] == False:
                return False
            # not over one peg
            if abs(row_end - row_start) != 2:
                return False
        return True

    def make_move(self, row_start, col_start, row_end, col_end):
        # marks start position false, end position true, and removes a peg
        self.board[row_start][col_start] = False
        self.board[row_end][col_end] = True
        self.pegs_left -= 1

        # Horizontal
        if row_start == row_end:
            # L to R or R to L
            if col_start < col_end:
                self.board[row_end][col_end-1] = False
            else:
                self.board[row_end][col_end+1] = False
        # Vertical        
        if col_start == col_end:
            # U to D or D to U
            if row_start < row_end:
                self.board[row_end - 1][col_end] = False
            else:
                self.board[row_end + 1][col_end] = False
        
    def final_message(self):
        # print message based on number of pegs left
        if self.pegs_left <= 2:
            print("You're a DigiPeg Genius!")
        if self.pegs_left > 2 and self.pegs_left <= 4:
            print("Not too shabby, rookie.")
        if self.pegs_left > 4 and self.pegs_left <= 6:
            print("That's nothing to write home about.")
        if self.pegs_left >= 7:
            print("You're a DigiPeg Igno-Ra-Moose")

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

    print(game)
    while (not game.game_over()):
        row_start = get_choice(1, rows, "Enter the row of the peg to move") - 1
        col_start = get_choice(
            1, columns, "Enter the column of the peg to move") - 1
        row_end = get_choice(1, rows, "Enter the row where the peg lands") - 1
        col_end = get_choice(
            1, columns, "Enter the column where the peg lands") - 1
        if game.legal_move(row_start, col_start, row_end, col_end):
            game.make_move(row_start, col_start, row_end, col_end)
        else:
            print("Sorry.  That move is not allowed.")
        print()
        print(game)

    game.final_message()
    
main()
