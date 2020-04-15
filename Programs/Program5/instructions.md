## Learning Outcomes

    Utilize 2D NumPy arrays to solve a problem.
    Utilize object-oriented programming to solve a problem.

# Peg Rectangle Solitaire

    Cracker Barrel restaurants typically set out a free table game called Peg Triangle Solitaire.

    For this assignment, you will implement a similar game that we shall call DigiPeg Solitaire. In DigiPeg Solitaire, the user can specify how many rows [1-9] and how many columns [1-9] the board should have.

## Legal Move
    In DigiPeg Solitaire, pegs can jump over an adjacent peg into an empty space. The jumping peg, the adjacent peg and the empty space must be in a straight line as in Peg Triangle Solitaire. The potential direction for a peg to jump is over, under, left, or right.

    When a jump is made the adjacent peg (the peg that was jumped over) is removed.

    The game is over when no more moves are possible.
    
## FINAL MESSAGE:
    When 2 or fewer pegs remain when the game ends, the message You're a DigiPeg Genius! 

    When 4 or fewer pegs remain, the message Not too shabby, rookie. 

    When 6 pegs remain, the message That's nothing to write home about.

    When 7 or more pegs remain, the message You're a DigiPeg Igno-Ra-Moose.



# Grading - 100 points

    10 points. The game_won method is correct. (All or nothing.)

    10 points. The final_message method is correct. (3 points off for each incorrect case up to 10 points.)
    
    40 points. The legal_move method returns True correctly. (5 points off for not identifying a legal jump in each of the eight directions.)
    
    20 points. The legal_move method returns False correctly. (10 points off for each type of illegal jump that is identified as a legal one up to 20 points.)

    10 points. The make_move method is correct. (All of nothing.)

    10 points - The methods you write are properly commented, easy to understand and do not contain unnecessary code. (3 points for each type of improvement up to 10 points.)
