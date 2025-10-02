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
