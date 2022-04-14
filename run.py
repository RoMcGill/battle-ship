# imported libraries
import random
from pyfiglet import figlet_format
import os
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('leaderboard').sheet1

# constant variables
SHIP_SIZES = [2, 3, 3, 4, 5]
USER_BOARD = [[' '] * 8 for i in range(8)]
COMP_BOARD = [[' '] * 8 for i in range(8)]
USER_PLAY_BOARD = [[' '] * 8 for i in range(8)]
COMP_PLAY_BOARD = [[' '] * 8 for i in range(8)]
NAVIGATION = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
W = "<winner<"
L = "<looser<"


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
    print('CAN YOU STATE IF YOU WON OR LOST, FOR OUR RECORDS')
    answer = input('ENTER W OR L:\n ').upper()
    while True:
        if answer == "W":
            update_sheet(W)
            break
        elif answer == "L":
            update_sheet(L)
            return False
        else:
            print('PLEASE ENTER W OR L')
            answer = input('ENTER W OR L:\n').upper()


def username_input():
    """
    Collects the user name input,
    """
    global player_name
    player_name = input('ENTER YOUR SECOND NAME SOLDIER!:\n')    
    print(f'GREAT TO SEE YOU ON BACK THE FRONTLINE RECON OFFICER {player_name}\n'.upper())
    return player_name


def update_sheet(data):
    """
    Update worksheet with new players name
    """
    player_name = SHEET.worksheet("leaderboard")
    
    player_name.append_row([data])


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
                        # place ship
                        if orientation == 'H':
                            for i in range(column, column + ship_size):
                                board[row][i] = 'X'
                        else:
                            for i in range(row, row + ship_size):
                                board[i][column] = 'X'
                        break

            else:
                Place_ship = True
                print(f"WHERE DO YOU WANT THIS {ship_size} MAN SHIP TO DOCK {player_name}\n")
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


def user_action(Place_ship):
    """
    gives user input, provides errors
    if ships are placed
    incorrectly (outside of the board)

    """
    if Place_ship == True:
        while True:
            try:
                orientation = input(f'DO YOU WANT OUR SHIPS HORIZONTAL OR VERTICAL {player_name}\n (H or V):\n').upper()
                if orientation == 'H' or orientation == 'V':
                    break
            except TypeError:
                print('(V or H) ARE YOUR OPTIONS')
        while True:
            try:
                row = input(f'WHAT ROW DO YOU WANT THIS SHIP PLACED IN {player_name}\n')
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('please enter a number between 1 and 8')
        while True:
            try:
                column = input(f'WHAT COLUMN DO YOU WANT THIS SHIP PLACED IN {player_name}\n').upper()
                if column in 'ABCDEFGH':
                    column = NAVIGATION[column]
                    break
            except KeyError:
                print('please enter a valid letter between A-H')
        return row, column, orientation
    else:
        while True:
            try:
                row = input(f'WHAT ROW WOULD YOU LIKE TO ATTACK? {player_name}\n')
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('enter a valid number between 1 - 8 ')
        while True:
            try:
                column = input('enter the column of the ship:\n').upper()
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


def clearConsole():
    """
    housekeeping, this clears the terminal
    when called for a cleener look and feel.
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


username_input()

def landing_page():
    print(figlet_format("Battle Ship", font = "standard"))
    print(figlet_format("WARZONE", font = "standard"))
    print(f"Welcome to the warzone {player_name}")
    print("Your objective is to strategically place your ships where they stand the \nbest chance of survival")
    print("You must tap into your powers of remote viewing to visualise where the enemie \nships are docked and \nreport their coordinates back to us.")
    print("We will take it from there!")
    answer = input('SHOW LEADERBOARD (L) CONTINUE (C):\n').upper()
    while True:
        if answer == "L":
            row_1 = SHEET.row_values(1)
            row_2 = SHEET.row_values(2)
            row_3 = SHEET.row_values(3)
            row_4 = SHEET.row_values(4)
            row_5 = SHEET.row_values(5)
            row_6 = SHEET.row_values(6)
            row_7 = SHEET.row_values(7)
            row_8 = SHEET.row_values(8)
            row_9 = SHEET.row_values(9)
            row_10 = SHEET.row_values(10)
            row_11 = SHEET.row_values(11)
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
            break
        elif answer == "C":

            return False
        else:
            print('PLEASE ENTER L OR C')
            answer = input('SHOW LEADERBOARD (L) CONTINUE (C):\n').upper()


    print(figlet_format("Ready ?", font = "standard"))
    answer = input('ENTER Y OR N:\n').upper()
    while True:
        if answer == "Y":
            update_sheet(player_name)
            break
        elif answer == "N":
            print('YOU WERE A GOOD SOLDIER!')
            return False
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

Place_ships(COMP_BOARD)
#show_board(COMP_BOARD)
#clearConsole()
show_board(USER_BOARD)
Place_ships(USER_BOARD)

while True:
    #player turn
    while True:
        print('Guess a battleship location')
        show_board(USER_PLAY_BOARD)
        turn(USER_PLAY_BOARD)
        break
    if count_score(USER_PLAY_BOARD) == 17:
        print(figlet_format("WINNER", font = "standard"))
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
    #computer turn
    while True:
        turn(COMP_PLAY_BOARD)
        break           
    show_board(COMP_PLAY_BOARD)   
    if count_score(COMP_PLAY_BOARD) == 17:
        print(figlet_format("LOOSER!", font = "standard"))
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

