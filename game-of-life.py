import random
import time

dead = 0
alive = 1

def dead_state(width, height):
    """
    width is number of rows and height is how long each row is 
    """
    deadboard = [[dead for _ in range(width)] for _ in range(height)]
    return deadboard

def random_state(width, height):
    dead_prob = 0.5
    """
    Will return board with each state either dead or alive with probability dead_prob
    """
    board = dead_state(width, height)
    for i in range(height):
        for j in range(width):
            rand = random.random()
            if rand > dead_prob:
                board[i][j] = 1
    print(board)
    return board

def board_height(board):
    return len(board)

def board_width(board):
    return len(board[0])

def render(board):
    display_lines = [ '|' for i in range(board_height(board)) ];
    
    for i in range( board_height(board) ):
        for elt in board[i]:
            if elt == dead:
                display_lines[i] +=  u"\u2591"*7
            elif elt == alive:
                display_lines[i] += u"\u2588"*7

    print('/' + '*-----*'*board_width(board) + '\\')

    for l in display_lines:
        print(l + '|')
        print(l + '|')
        print(l + '|')

    print('\\' + '*-----*'*board_width(board) + '/')

def next_board(initial_board):
    width = board_width(initial_board)
    height = board_height(initial_board)
    new_board = dead_state(width, height)
    for row in range(height):
        for col in range(width):
            new_board[row][col] = next_cell_value(row, col, initial_board)
    return new_board

def next_cell_value( row, col, board  ):
    #NOTE here i have used a wraparound method for the edges and corners, 
    #TODO: implement a dead end method
    width = board_width(board)
    height = board_height(board)
    neighbour_sum = 0
    for n_row in range(row-1, (row+1)+1):
        for n_col in range( col-1, col+1+1 ):
            if n_row < 0 or n_row >= height: continue
            if n_col < 0 or n_col >= width: continue
            if n_col == col and n_row == row: continue

            if board[n_row][n_col] == alive:
                neighbour_sum += 1
    
    if neighbour_sum == 3 and board[row][col] == dead :
        new_value = alive
    elif board[row][col] == alive:
        if neighbour_sum < 2 or neighbour_sum > 3:
            new_value = dead
        else:
            new_value = alive
    else: 
        new_value = dead
    return new_value

def run_forever(initial_board):
    new_board = initial_board
    while True:
        render(new_board)
        new_board = next_board(new_board)
        time.sleep(0.2)

#run_forever( [[0,0,0,0,0],[0,0,0,0,0],[0,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0]] )

def import_board(filepath):
    with open(filepath, 'r') as f:
        lines = [l.rstrip() for l in f.readlines()]

    width = len(lines[0])
    height = len(lines)

    board = dead_state(width, height)
    print(board)

    for i in range(height):
        for j in range(width):
            board[i][j] = int(lines[i][j])
    return board

run_forever(import_board('./glider_gun.txt'))