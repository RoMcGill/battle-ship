import random

SHIP_SIZES = [2,3,3,4,5]
USER_BOARD = [[' '] * 8 for i in range(8)]
COMP_BOARD = [[' '] * 8 for i in range(8)]
USER_PLAY_BOARD = [[' '] * 8 for i in range(8)]
COMP_PLAY_BOARD = [[' '] * 8 for i in range(8)]
NAVIGATION = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}

def show_board(board):
    print('  a b c d e f g h')
    print('  -+-+-+-+-+-+-+-+')
    row_no = 1
    #loop through row
    for row in board:
        # creating the grid formatting decimal, string and joining (|) to each row 
        print('%d|%s|' % (row_no,'|'.join(row)))
        row_no += 1

def Place_ships(board):
    for ship_size in SHIP_SIZES:
        while True:
            if board == COMP_BOARD:
                row, column, orientation = random.choice(['h', 'v']), random.randint(0, 7), random.randint(0, 7)
                if check_ship_size(ship_size, row, column, orientation):
                    if ship_overlap(ship_size, row, column, orientation) == False:
                        #place ship
                        if orientation == 'h':
                            for i in range (column, column + ship_size):
                                board[row][i] = 'x'
                        else:
                            for i in range(row, row + ship_size):
                                board[i][column] = 'x'
                        break

            else:
                Place_ships = True
                print(f"place ship with size of {ship_size}") 
                row, column, orientation = user_action(Place_ships)
                if check_ship_size(ship_size, row, column, orientation):
                    if ship_overlap(ship_size, row, column, orientation) == False:
                        #place ship
                        if orientation == 'h':
                            for i in range (column, column + ship_size):
                                board[row][i] = 'x'
                        else:
                            for i in range(row, row + ship_size):
                                board[i][column] = 'x'
                        break

def check_ship_size(SHIP_SIZES, row, column, orientation):
    if orientation == 'h':
        if column + SHIP_SIZES > 8:
            return False
        else:
            return True
    #else:
        #if row + SHIP_SIZES > 8:
            #return False
        #else:
            #return True


def ship_overlap(SHIP_SIZES, row, column, orientation):
    if orientation == 'h':
        for i in range(column, column + ship_size):
            if board[row][i] == 'x':
                return True
    else:
        for i in range(row,row + ship_size):
            if board[i][column] == 'x':
                return True
    return False

def user_action(Place_ships):
    if Place_ships == True:
        while True:
            try:
                orientation = input('enter orientation (h or v): ')
                if orientation == 'h' or orientation == 'v':
                    break
            except TypeError:
                print('please enter v or h')
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
                column = input('enter the column you would like to place your ship:')
                if column in 'abcdefgh':
                    column = NAVIGATION[column]
                    break
            except KeyError:
                print('please enter a valid letter between a-h')
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
                column = input('enter the column of the ship: ')
                if column in 'abcdefgh':
                    column = NAVIGATION[column]
                    break
            except KeyError:
                print('enter a valid letter between a-h')

def count_score(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'x':
                count +=1
    return count

def turn(board):
    if board == USER_PLAY_BOARD:
        row, column = user_action(USER_PLAY_BOARD)
        if board[row][column] == '-':
            turn(board)
        elif board [row][column] == 'x':
            turn(board)
        elif COMP_BOARD[row][column] == 'x':
            board[row][column] = 'x'
        else:
            board[row][column] = '-'
    else:
        row, column = random.randint(0,7), random.randint(0, 7)
        if board[row][column] == '-':
            turn(board)
        elif board [row][column] == 'x':
            turn(board)
        elif COMP_BOARD[row][column] == 'x':
            board[row][column] = 'x'
        else:
            board[row][column] = '-'

Place_ships(COMP_BOARD)
show_board(COMP_BOARD)
show_board(USER_BOARD)
Place_ships(USER_BOARD)

#while True:
