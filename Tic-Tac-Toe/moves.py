from free_fields import make_list_of_free_fields
from board import display_board
from victory import victory_for


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.

    # Accepts, checks, and updates user's move/decision
    while True: 
        try: 
            move = int(input("\nEnter the square you want to make your move in: ")) # Accepts
        except ValueError: 
            print("Please enter a positive integer between 1 and 9.")
            continue
        
        if move not in range(1, 10): 
            print("Invalid square. Choose between 1 and 9.")
            continue # Checks if choosen square is valid
        
        # Convert the 1–9 number into (row, col)
        if move <= 3:
            row, col = 0, move - 1
        elif move <= 6:
            row, col = 1, move - 4
        else:
            row, col = 2, move - 7

        # Check if this (row, col) is in free fields
        free_fields = make_list_of_free_fields(board)
        if (row, col) not in free_fields:
            print("That square is already taken. Try again.")
            continue
        
        # If valid → update the board
        else: 
            board[row][col] = 'o' # updates   
        
        display_board(board)
        print("You have played.")
        result = victory_for(board, 'o')
        free_fields = make_list_of_free_fields(board)  # refresh list of empty squares again
        
        if result != 'Draw':   # player wins
            print(result)
        elif not free_fields:   # no more spaces → draw
            print("It's a draw!")
        else:
            draw_move(board)   # continue game
        break


def draw_move(board):
#   The function draws the computer's move and updates the board.
    from random import randrange

    free_fields = make_list_of_free_fields(board)
    while True:
        row = randrange(3)
        column = randrange(3)

        if (row, column) in free_fields:  # <-- check directly against free slots
            board[row][column] = 'x'
            print(f"Computer's move = {row * 3 + column + 1}")
            break  # stop looping once move is made     

    display_board(board)
    print("Computer played.")
    result = victory_for(board, 'x') # check for computer win
    free_fields = make_list_of_free_fields(board) # to check for empty space again

    if result != 'Draw':   # computer wins
        print(result)
    elif not free_fields:   # draw
        print("It's a draw!")
    else:
        enter_move(board)   # continue game
