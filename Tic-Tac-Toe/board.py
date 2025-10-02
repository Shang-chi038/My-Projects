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
