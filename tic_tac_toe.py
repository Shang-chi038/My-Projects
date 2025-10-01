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
            try: 
                move = int(input("Please enter a positive integer from between 1 to 9, inclusive: "))
            # incase
            except: 
                print("Sorry, cannot help you.")
                break
        
        if 0 < move < 10: # Checks
                if move < 4:
                    board[0][move -1] = 'o' # updates
                elif move < 7: 
                    board[1][move - 4] = 'o' 
                elif move < 10: 
                    board[2][move - 7] = 'o' 
    
                display_board(board)
                print("You have played.")
                victory_for(board, 'x')
                draw_move(board)
                break
        else: continue


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
    
    
    return 'x & o Draw'


def draw_move(board):
#   The function draws the computer's move and updates the board.
    from random import randrange

    while True:
        row = randrange(3)
        column = randrange(3)
        if row == 0: computers_move = column + 1
        elif row == 1: computers_move = column + 4
        elif row == 2: computers_move = column + 7

        for rows, columns in make_list_of_free_fields(board):
            print("Computer's move =", computers_move)
            if board[row][column] != board[rows][columns]: 
                continue
            elif board[row][column] == board[rows][columns]:
                    board[2][computers_move - 7] = 'x'
                

    display_board(board)
    print("Computer played.")
    victory_for(board, 'x')
    enter_move(board)


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
