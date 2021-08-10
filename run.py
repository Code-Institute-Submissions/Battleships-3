from random import randint

"""
Build Board
"""
board = []
for i in range(0, 5):
    board.append(['O '] * 5) 


def print_board(board):
    """
    Prints board to the terminal in a 5x5 format
    """
    print("""
░█▀▀█ █▀▀█ ▀▀█▀▀ ▀▀█▀▀ █── █▀▀ █▀▀ █──█ ─▀─ █▀▀█ █▀▀ 
░█▀▀▄ █▄▄█ ──█── ──█── █── █▀▀ ▀▀█ █▀▀█ ▀█▀ █──█ ▀▀█ 
░█▄▄█ ▀──▀ ──▀── ──▀── ▀▀▀ ▀▀▀ ▀▀▀ ▀──▀ ▀▀▀ █▀▀▀ ▀▀▀""")
    print("======================================================")
    print("======================================================")
    for row in board: 
        print(''.join(row))
    print("======================================================")
    print("======================================================")
        



def set_game_board(board):
    """
    Populates and returns random position within board, allows for
    user input and calculates whether or not the user input is a hit or miss. 
    Validates user input to ensure that it is within range 0,4.
    """
    computer_choice_row = int(randint(0,4))
    computer_choice_column = int(randint(0,4))
    print(computer_choice_row, computer_choice_column)
   
    user_guesses = 0

    while user_guesses < 5:
        guess_row = int(input('Guess Row Position: '))
        guess_column = int(input('Guess Column Position: '))

        computer_choice = computer_choice_column, computer_choice_row
        user_choice = guess_column, guess_row

        if computer_choice == user_choice:
            print ("You hit the battleship!!")
            break

        elif guess_row not in range(5) or guess_column not in range(5):
                print (f'The numbers you entered are outside of the board! You entered {guess_row} and {guess_column}. Numbers entered must be between 0 and 4')
        
        elif board[guess_column][guess_row] == 'X ':
            print("""🆈 🅾 🆄  🅰 🅻 🆁 🅴 🅰 🅳 🆈  🅼 🅸 🆂 🆂 🅴 🅳  🆃 🅷 🅴  🆃 🅰 🆁 🅶 🅴 🆃   🅷 🅴 🆁 🅴❗❗""")
            
            
        else:
            print("""🆈 🅾 🆄  🅼 🅸 🆂 🆂 🅴 🅳  🆃 🅷 🅴  🅱 🅰 🆃 🆃 🅻 🅴 🆂 🅷 🅸 🅿 ❗❗""")
            board[guess_row][guess_column] = 'X '
            print_board(board)
            user_guesses +=1
            print (f"{user_guesses} Guesses of 5 Guesses Used!!")
            if user_guesses == 5:
                print("Game Over You Only Have 5 Turns!!!!")
       


    
    
    
        
    



def start_game():
    """
    Starts Game
    """
    #build_board()
    print_board(board)
    set_game_board(board)
    #game_loop(board)
    #validate_input(user_choice)
    #check_user_input(guess_column,guess_row)


start_game()