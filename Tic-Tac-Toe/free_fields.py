def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    
    list_of_free_fields = []
    
    for row in range(3):
        for column in range(3):
            if board[row][column] not in ['x', 'o']:
                list_of_free_fields.append((row, column))
    
    return list_of_free_fields
