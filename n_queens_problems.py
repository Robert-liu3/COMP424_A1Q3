import random

def create_board(n):
    board = []
    for i in range (n):
        board.append(random.randint(0, n-1))
    return board

def attacking_pairs(board):
    n = len(board)
    num_pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if (board[i] == board[j]) or (abs(board[i] - board[j]) == abs(i - j)):
                num_pairs += 1
    return num_pairs

def hill_climbing(n):
    current_board = create_board(n)
    current_attacking_pairs = attacking_pairs(current_board)

    #while loop is checking if your board is empty or not
    while():
        if current_attacking_pairs == 0:
            return current_board
        
