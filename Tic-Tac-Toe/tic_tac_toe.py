from board import display_board
from moves import draw_move

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
