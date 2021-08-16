from random import randint
from constants import BATTLESHIP_TEXT, GAME_OVER, GAME_OVER, DASH, BATTLESHIP, CONGRAT, WIN, HIT

"""
Build Board
"""
board = []

def build_board(row, col):
    for i in range(0, row):
        board.append(['O '] * col)


def print_board():
    """
    Prints board to the terminal in a 5x5 format
    """

    print(DASH)
    print(DASH)
    for row in board:
        print(''.join(row))
    print(DASH)
    print(DASH)


def generate_ship_positions(rows, columns):
    """
    Populates and returns random position within board.
    """
    computer_choice_row = int(randint(0, 4))
    computer_choice_column = int(randint(0, 4))
    return [computer_choice_row, computer_choice_column]


def set_game_board(no_of_ships, no_of_guesses, rows, cols):
    """
    sets the board with number of ships and ship locations. Checks to see if ships already placed in a selected position and does not place a ship in the same place twice.
    sets the number of guesses for each game dependant on level.
    """
    ship_locations = []
    ships_added = 0
    while ships_added < no_of_ships:
        location = generate_ship_positions(rows, cols)
        if location not in ship_locations:
            ships_added = ships_added + 1
            ship_locations.append(location)
    print(ship_locations)
    user_guesses = 0
    correct_guesses = 0

    while user_guesses < no_of_guesses:
        guess_row = int(input('Guess Row Position: '))
        guess_column = int(input('Guess Column Position: '))
        user_choice = [guess_row, guess_column]

        if guess_row not in range(rows) or guess_column not in range(cols):
            print(f'The numbers you entered are outside of the board! You entered {guess_row} and {guess_column}. Numbers entered must be between 0 and {rows - 1}')
        elif board[guess_row][guess_column] == 'H ':
            print("""𝕐𝕠𝕦 𝔸𝕝𝕣𝕖𝕒𝕕𝕪 Guessed 𝕋𝕙𝕖 𝕋𝕒𝕣𝕘𝕖𝕥 ℍ𝕖𝕣𝕖❕❕❕""")
            print_board()
        elif user_choice in ship_locations:
            correct_guesses = correct_guesses + 1
            board[guess_row][guess_column] = 'H '
            user_guesses += 1
            print(HIT)
            if correct_guesses == no_of_ships:
                 print(CONGRAT)
                 print(WIN)
                 break
        elif board[guess_row][guess_column] == 'X ':
            print("""𝕐𝕠𝕦 𝔸𝕝𝕣𝕖𝕒𝕕𝕪 𝕄𝕚𝕤𝕤𝕖𝕕 𝕋𝕙𝕖 𝕋𝕒𝕣𝕘𝕖𝕥 ℍ𝕖𝕣𝕖❕❕❕""")
            print_board()
        else:
            print("""𝕐𝕠𝕦 𝕄𝕚𝕤𝕤𝕖𝕕 𝕋𝕙𝕖 𝕥𝕒𝕣𝕘𝕖𝕥 ℍ𝕖𝕣𝕖❕❕❕""")
            board[guess_row][guess_column] = 'X '
            print_board()
            user_guesses += 1
            print(f"{user_guesses} Guesses of {no_of_guesses} Guesses Used!!")
            if user_guesses == no_of_guesses:
                print(GAME_OVER)
                print(f"Game Over You Only Have {no_of_guesses} Turns!!!!")
                break


def get_level_and_validate():
    level_select = int(input())
    if level_select < 0 or level_select > 5:
        print(f'You must choose a level between 1 and 5. You chose {level_select} !! Please enter again! ')
        return get_level_and_validate()
    else:
        return level_select

def get_level_params(level):
    rows = None 
    cols = None
    no_of_ships = None
    no_of_guesses = None
    if level == 1:
        [rows, cols] = [5,5]
        no_of_ships = 6
        no_of_guesses = 5
    elif level == 2:
        [rows, cols] = [6,6]
        no_of_ships = 5
        no_of_guesses = 5
    elif level == 3:
        [rows, cols] = [7,7]
        no_of_ships = 3
        no_of_guesses = 5
    elif level == 4:
        [rows, cols] = [7,7]
        no_of_ships = 3
        no_of_guesses = 5
    elif level == 5:
        [rows, cols] = [7,7]
        no_of_ships = 2
        no_of_guesses = 4
    return rows, cols, no_of_ships, no_of_guesses

def start_game():
    """
    Starts Game
    """

    print(BATTLESHIP)
    print(BATTLESHIP_TEXT)
    print('Please choose a number between 1 and 5. 1 being easy and 5 being the hardest:  ')
    level = get_level_and_validate()
    rows, cols, no_of_ships, no_of_guesses = get_level_params(level)

    build_board(rows, cols)
    print_board()
    set_game_board(no_of_ships, no_of_guesses, rows, cols)

start_game()
