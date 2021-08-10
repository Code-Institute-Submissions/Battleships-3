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
        



def guess_position(board):
    """
    Populates and returns random position within board, allows for
    user input and calculates whether or not the user input is a hit or miss.
    """
    computer_choice_row = int(randint(0,4))
    computer_choice_column = int(randint(0,4))
    print(computer_choice_row, computer_choice_column)
    
    
    guess_row = int(input('Guess Row Position: '))
    guess_column = int(input('Guess Column Position: '))
    computer_choice = computer_choice_column, computer_choice_row
    user_choice = guess_column, guess_row

    if computer_choice == user_choice:
        print("Hit")
        
    else:
        print('miss')
        board[guess_row][guess_column] = 'X'
        print_board(board)
#def validate_input(user_choice):
#    """
#    Checks that input entered into the terminal is an integer between 0 and 4.
#    """
 #   if input >= 5:
 #       print('Value entered should be a number between 0 and 4')
    




print_board(board)
guess_position(board)
#validate_input(user_choice)