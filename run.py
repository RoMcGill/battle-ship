import random
from pyfiglet import figlet_format
import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('leaderboard')
SHEET1 = GSPREAD_CLIENT.open('leaderboard').sheet1

# constant variables
SHIP_SIZES = [2, 3, 3, 4, 5]
USER_BOARD = [[' '] * 8 for i in range(8)]
COMP_BOARD = [[' '] * 8 for i in range(8)]
USER_PLAY_BOARD = [[' '] * 8 for i in range(8)]
COMP_PLAY_BOARD = [[' '] * 8 for i in range(8)]
NAVIGATION = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
W = ",winner<"
L = ",looser<"


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


def did_you_win():
    """
    asks user to verify if they have
    won or not, if they have, their name gets
    put on the winners board.
    """
    print('CAN YOU STATE IF YOU WON OR LOST,')
    print('SO WE CAN ADD YOU TO OUR WINNERSBOARD')
    answer = input('ENTER W OR L:\n ').upper()
    while True:
        if answer == "W":
            update_sheet(PLAYER_NAME)
            break
        elif answer == "L":
            return False
        else:
            print('PLEASE ENTER W OR L')
            answer = input('ENTER W OR L:\n').upper()


def username_input():
    """
    Collects the user name input,
    """
    global PLAYER_NAME
    PLAYER_NAME = input('ENTER YOUR SECOND NAME SOLDIER!:\n')
    print('GREAT TO SEE YOU ON BACK THE FRONTLINE')
    print(f'RECON OFFICER {PLAYER_NAME}')
    return PLAYER_NAME


def update_sheet(data):
    """
    Update worksheet with new players name
    """
    PLAYER_NAME = SHEET.worksheet("leaderboard")
    PLAYER_NAME.append_row([data])


def place_ships(board):
    """
    places ships, for computer in random variations
    h for horzontal and v for vertical.
    function also ensures no overlap of ships or that
    no ships are bing placed outside the grid.
    """
    for ship_size in SHIP_SIZES:
        while True:
            if board == COMP_BOARD:
                orientation, row, column = random.choice(
                    ['H', 'V']
                    ), random.randint(0, 7), random.randint(0, 7)
                if check_ship_size(
                        ship_size,
                        row,
                        column,
                        orientation):
                    if ship_overlaps(
                            board,
                            row,
                            column,
                            orientation,
                            ship_size,) is False:
                        # place ship
                        if orientation == 'H':
                            for i in range(column, column + ship_size):
                                board[row][i] = 'X'
                        else:
                            for i in range(row, row + ship_size):
                                board[i][column] = 'X'
                        break

            else:
                place_ship = True
                print(f"WHERE DO YOU WANT THIS {ship_size}")
                print(f"MAN SHIP TO DOCK {PLAYER_NAME}")
                row, column, orientation = user_action(place_ship)
                if check_ship_size(ship_size, row, column, orientation):
                    if ship_overlaps(
                            board,
                            row,
                            column,
                            orientation,
                            ship_size,) is False:
                        # place ship
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
        if column + SHIP_SIZE > 8:
            return False
        else:
            return True
    else:
        if row + SHIP_SIZE > 8:
            return False
        else:
            return True


# find bug in here that thinks ships are overlapping
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


def user_action(place_ship):
    """
    gives user input, provides errors
    if ships are placed
    incorrectly (outside of the board)

    """
    if place_ship is True:
        while True:
            try:
                print('DO YOU WANT THIS SHIP')
                print('HORIZONTAL OR VERTICAL')
                orientation = input(f'{PLAYER_NAME}\n (H or V):\n').upper()
                if orientation == 'H' or orientation == 'V':
                    break
            except TypeError:
                print('(V or H) ARE YOUR OPTIONS')
        while True:
            try:
                print('WHAT ROW DO YOU WANT THIS SHIP PLACED IN')
                row = input(f'{PLAYER_NAME}\n')
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('please enter a number between 1 and 8')
        while True:
            try:
                print('WHAT COLUMN DO YOU WANT THIS SHIP PLACED IN')
                column = input(f'{PLAYER_NAME}\n').upper()
                if column in 'ABCDEFGH':
                    column = NAVIGATION[column]
                    break
            except KeyError:
                print('please enter a valid letter between A-H')
        return row, column, orientation
    else:
        while True:
            try:
                print('WHAT ROW WOULD YOU LIKE TO ATTACK?')
                row = input(f'{PLAYER_NAME}\n')
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('enter a valid number between 1 - 8 ')
        while True:
            try:
                column = input('WHAT COLUMN SHOULD WE FIRE ON:\n').upper()
                if column in 'ABCDEFGH':
                    column = NAVIGATION[column]
                    break
            except KeyError:
                print('enter a valid letter between A-H')
        return row, column


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


username_input()


def landing_page():
    """
    a main menu to display the rules of the game
    and give the user an option to view the winnerboard
    or continue
    """
    print(figlet_format("Battle Ship", font="standard"))
    print(figlet_format("WARZONE", font="standard"))
    print(f"Welcome to the warzone {PLAYER_NAME}")
    print("Your objective is to strategically place your ships")
    print("where they stand the best chance of survival")
    print("You must tap into your powers of remote viewing to")
    print("visualise where the enemie ships are docked and")
    print("report their coordinates back to us.")
    print("We will take it from there!")
    answer = input('SHOW WINNERSBOARD (W) CONTINUE (C):\n').upper()
    while True:
        if answer == "W":
            row_1 = SHEET1.row_values(1)
            row_2 = SHEET1.row_values(2)
            row_3 = SHEET1.row_values(3)
            row_4 = SHEET1.row_values(4)
            row_5 = SHEET1.row_values(5)
            row_6 = SHEET1.row_values(6)
            row_7 = SHEET1.row_values(7)
            row_8 = SHEET1.row_values(8)
            row_9 = SHEET1.row_values(9)
            row_10 = SHEET1.row_values(10)
            row_11 = SHEET1.row_values(11)
            row_12 = SHEET1.row_values(12)
            row_13 = SHEET1.row_values(13)
            row_14 = SHEET1.row_values(14)
            row_15 = SHEET1.row_values(15)
            row_16 = SHEET1.row_values(16)
            row_17 = SHEET1.row_values(17)
            row_18 = SHEET1.row_values(18)
            row_19 = SHEET1.row_values(19)
            row_20 = SHEET1.row_values(20)
            row_21 = SHEET1.row_values(21)
            print(row_1)
            print(' ')
            print(row_2)
            print(row_3)
            print(row_4)
            print(row_5)
            print(row_6)
            print(row_7)
            print(row_8)
            print(row_9)
            print(row_10)
            print(row_11)
            print(row_12)
            print(row_13)
            print(row_14)
            print(row_15)
            print(row_16)
            print(row_17)
            print(row_18)
            print(row_19)
            print(row_20)
            print(row_21)
            break
        elif answer == "C":

            return False
        else:
            print('PLEASE ENTER W OR C')
            answer = input('SHOW LEADERBOARD (W) CONTINUE (C):\n').upper()
    print(figlet_format("Ready ?", font="standard"))
    answer = input('ENTER Y OR N:\n').upper()
    while True:
        if answer == "Y":
            break
        elif answer == "N":
            print('YOU WERE A GOOD SOLDIER!')
            landing_page()
        else:
            print('PLEASE ENTER Y OR N')
            answer = input('ENTER Y OR N: \n').upper()


landing_page()


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
        elif USER_BOARD[row][column] == 'X':
            board[row][column] = 'X'
        else:
            board[row][column] = '-'


place_ships(COMP_BOARD)
show_board(USER_BOARD)
place_ships(USER_BOARD)


while True:
    # player turn
    while True:
        print('Guess a battleship location')
        show_board(USER_PLAY_BOARD)
        turn(USER_PLAY_BOARD)
        break
    if count_score(USER_PLAY_BOARD) == 17:
        print(figlet_format("WINNER", font="standard"))
        did_you_win()
        print('YOU SAVED ALOT OF LIVES OUT THERE TODAY SOLDIER')
        print('WOULD YOU LIKE TO GET BACK IN THE ACTION?')
        answer = input('ENTER Y OR N:\n').upper()
        while True:
            if answer == "Y":
                landing_page()
            elif answer == "N":
                print('YOU WERE A GOOD SOLDIER!')
                landing_page()
            else:
                print('PLEASE ENTER Y OR N')
                answer = input('ENTER Y OR N:\n').upper()
            break
    # computers turn
    while True:
        turn(COMP_PLAY_BOARD)
        break
    show_board(COMP_PLAY_BOARD)
    if count_score(COMP_PLAY_BOARD) == 17:
        print(figlet_format("LOOSER!", font="standard"))
        did_you_win()
        print("WE MAY HAVE LOST THE BATTLE, BUT NOT THE WAR!")
        print('WOULD YOU LIKE TO GET BACK IN THE ACTION?')
        answer = input('ENTER Y OR N:\n').upper()
        while True:
            if answer == "Y":
                landing_page()
            elif answer == "N":
                print('YOU WERE A GOOD SOLDIER!')
                landing_page()
            else:
                print('PLEASE ENTER Y OR N')
                answer = input('ENTER Y OR N: \n').upper()
            break
        break
