import random
from pyfiglet import figlet_format
import os

SHIP_SIZES = [2, 3, 3, 4, 5]
USER_BOARD = [[' '] * 8 for i in range(8)]
COMP_BOARD = [[' '] * 8 for i in range(8)]
USER_PLAY_BOARD = [[' '] * 8 for i in range(8)]
COMP_PLAY_BOARD = [[' '] * 8 for i in range(8)]
NAVIGATION = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}


def show_board(board):
    """
    creates board layout, 
    """
    print('  A B C D E F G H')
    print('  -+-+-+-+-+-+-+-+')
    row_no = 1
    for row in board:
        # creating the grid formatting
        # decimal, string and joining (|) to each space in row
        # to create columns. 
        print('%d|%s|' % (row_no, '|'.join(row)))
        row_no += 1


def Place_ships(board):
    """
    places ships, for computer in random variations
    h for horzontal and v for vertical.
    function also ensures no overlap of ships or that
    no ships are bing placed outside the grid.
    """
    for ship_size in SHIP_SIZES:
        while True:
            if board == COMP_BOARD:
                orientation, row, column = random.choice(['H', 'V']), random.randint(0, 7), random.randint(0, 7)
                if check_ship_size(ship_size, row, column, orientation):
                    if ship_overlaps(board, row, column, orientation, ship_size,) == False:
                        #place ship
                        if orientation == 'H':
                            for i in range(column, column + ship_size):
                                board[row][i] = 'X'
                        else:
                            for i in range(row, row + ship_size):
                                board[i][column] = 'X'
                        break

            else:
                Place_ship = True
                print(f"place ship with size of {ship_size} spaces to the board")
                row, column, orientation = user_action(Place_ship)
                if check_ship_size(ship_size, row, column, orientation):
                    if ship_overlaps(board, row, column, orientation, ship_size,) == False:
                        #place ship
                        if orientation == 'H':
                            for i in range(column, column + ship_size):
                                board[row][i] = 'X'
                        else:
                            for i in range(row, row + ship_size):
                                board[i][column] = 'X'
                        show_board(USER_BOARD)
                        break


def check_ship_size(SHIP_SIZE, row, column, orientation):
    """
    checks the lenght of each ship,
    if the whole ship does not fit in grid 
    it will return and try again and print 
    'ship does not fit'
    """
    if orientation == "H":
        if row + SHIP_SIZE > 8:
            print('ship does not fit')
            return False
        else:
            return True
    else:
        if row + SHIP_SIZE > 8:
            return False
        else:
            return True

#
def ship_overlaps(board, row, column, orientation, ship_size):
    """
    checks for overlap in placed ships
    """
    if orientation == 'H':
        for i in range(column, column + ship_size):
            if board[row][i] == 'X':
                return True
    else:
        for i in range(row, row + ship_size):
            if board[i][column] == 'X':
                return True
    return False


def user_action(Place_ship):
    """
    gives user input, provides errors 
    if ships are placed 
    incorrectly (outside of the board)

    """
    if Place_ship == True:
        while True:
            try:
                orientation = input('enter orientation (H or V): ').upper()
                if orientation == 'H' or orientation == 'V':
                    break
            except TypeError:
                print('please enter V or H')
        while True:
            try:
                row = input('enter the row where you would like to place your ship: ')
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('please enter a number between 1 and 8')
        while True:
            try:
                column = input('enter the column you would like to place your ship:').upper()
                if column in 'ABCDEFGH':
                    column = NAVIGATION[column]
                    break
            except KeyError:
                print('please enter a valid letter between A-H')
        return row, column, orientation
    else:
        while True:
            try:
                row = input('enter the row 1 - 8 of the ships')
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('enter a valid number between 1 - 8 ')
        while True:
            try:
                column = input('enter the column of the ship: ').upper()
                if column in 'ABCDEFGH':
                    column = NAVIGATION[column]
                    break
            except KeyError:
                print('enter a valid letter between A-H')
        return row, column

#
def count_score(board):
    """
    counts correct hits 
    """
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


def turn(board):
    """
    defines whos 'go' it is 
    and when to pass onto the computer
    player then back to the user 
    """
    if board == USER_PLAY_BOARD:
        row, column = user_action(USER_PLAY_BOARD)
        if board[row][column] == '-':
            turn(board)
        elif board[row][column] == 'X':
            turn(board)
        elif COMP_BOARD[row][column] == 'X':
            board[row][column] = 'X'
        else:
            board[row][column] = '-'
    else:
        row, column = random.randint(0, 7), random.randint(0, 7)
        if board[row][column] == '-':
            turn(board)
        elif board[row][column] == 'X':
            turn(board)
        elif COMP_BOARD[row][column] == 'X':
            board[row][column] = 'X'
        else:
            board[row][column] = '-'


def clearConsole():
    """
    housekeeping, this clears the terminal
    when called for a cleener look and feel.
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def main():
    """
    main function to run all 
    functions in one place.
    """
    Place_ships(COMP_BOARD)
    clearConsole()
    #show_board(COMP_BOARD)
    print(figlet_format("Battle Ship", font = "standard"))
    show_board(USER_BOARD)
    Place_ships(USER_BOARD)


main()

# deciding the winner based on the data.
while True:
    #user turn
    while True:
        print('guess a battleship location')
        show_board(USER_PLAY_BOARD)
        turn(USER_PLAY_BOARD)
        break
    if count_score(USER_PLAY_BOARD) == 17:
        print('you win!')
        break
    #comp turn
    while True:
        turn(COMP_PLAY_BOARD)
        break
    show_board(COMP_PLAY_BOARD)
    if count_score(COMP_PLAY_BOARD) == 17:
        print('computer wins !!')
        break
