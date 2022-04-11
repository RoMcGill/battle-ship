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
    
show_board(USER_BOARD)

def Place_ships(board):
    pass

def check_ship_size():
    pass

def ship_overlap():
    pass

def user_action():
    pass

def count_score():
    pass

def turn(board):
    pass

#while True: