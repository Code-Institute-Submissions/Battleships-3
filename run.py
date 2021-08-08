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
        print(row)

print_board(board)