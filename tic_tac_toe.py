def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------+-------+-------+")
    for i in range(3):
        print("|\t" * 4)
        
        for k in range(3):
            print(f"|   {board[i][k]}   ", end='')
    
        print("|")
        print("|\t" * 4)
        print("+-------+-------+-------+")


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


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    
    list_of_free_fields = []
    
    for row in range(3):
        for column in range(3):
            if board[row][column] not in ['x', 'o']:
                list_of_free_fields.append((row, column))
    
    return list_of_free_fields



def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    diagonal1 = [board[0][0], board[1][1], board[2][2]] #\
    diagonal2 = [board[0][2], board[1][1], board[2][0]] #/

    vertical1 = [board[0][0], board[1][0], board[2][0]] #column1
    vertical2 = [board[0][1], board[1][1], board[2][1]] #column2
    vertical3 = [board[0][2], board[1][2], board[2][2]] #column3

    horizontal1 = [board[0][0], board[0][1], board[0][2]] #row1
    horizontal2 = [board[1][0], board[1][1], board[1][2]] #row2
    horizontal3 = [board[2][0], board[2][1], board[2][2]]  #row3

    if ((diagonal1.count(sign) == len(diagonal1)) 
        or (diagonal2.count(sign) == len(diagonal2)) 
        or (horizontal1.count(sign) == len(horizontal1)) 
        or (horizontal2.count(sign) == len(horizontal2)) 
        or (horizontal3.count(sign) == len(horizontal3)) 
        or (vertical1.count(sign) == len(vertical1)) 
        or (vertical2.count(sign) == len(vertical2))
        or (vertical3.count(sign) == len(vertical3))
        ):
        if sign == 'o': return 'You win'
        elif sign == 'x': return 'Computer wins'
    
    
    return 'Draw'


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


if __name__ == "__main__":
    from time import sleep
    global board 
    board = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    print("\n\nThis is a tic-tac-toe board below: ")
    display_board(board)

    print("\n\nYou are 'o' and the computer is 'x', and computer plays first.\nBEGIN!!!")

    sleep(3)
    # board = make_list_of_free_fields(board)
    draw_move(board)
