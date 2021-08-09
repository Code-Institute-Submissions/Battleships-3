from random import randint 
"""
Build Board
"""
board = []
for i in range(0, 5):
     board.append(['O'] * 5)


def print_board(board):
    """
    Prints board to the terminal in a 5x5 format
    """
    for row in board: 
        print(''.join(row))




def computer_choice(board):
    """
    Populates and returns random position within board 
    """
    computer_choice_row = randint(0,4)
    computer_choice_column = randint(0,4)


    return computer_choice_column, computer_choice_row

print_board(board)
computer_choice(board)