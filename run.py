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
    print(computer_choice_column, computer_choice_row)
    return computer_choice_column, computer_choice_row

    

def guess_position(board):
    """
    Asks user for input of column and row guess
    """
    guess_column = input('Guess Row Position: ')
    guess_row = input('Guess Column Position: ')
    return guess_column, guess_row


computer_guess = computer_choice(board)   
user_guess = guess_position(board)


def calculate_hit():
    if computer_guess == user_guess:
        print("Hit")
    #else:
        # print('miss')





print_board(board)
computer_choice(board)
guess_position(board)
calculate_hit()