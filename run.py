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

def Place_ships(USER_BOARD):
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

def check_ship_size(SHIP_SIZES, row, column, orientation):
    if orientation == 'h':
        if column + SHIP_SIZES > 8:
            return False
        else:
            return True
    else:
        if row + SHIP_SIZES > 8:
            return False
        else:
            return True


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

def user_action():
    pass

def count_score():
    pass

def turn(board):
    pass

while True: