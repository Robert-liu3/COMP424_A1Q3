import random

#create board where each index in the array represents a row, and the integer stored in the array represents a column
def create_board(n):
    board = []
    for i in range (n):
        board.append(random.randint(0, n-1))
    return board

#check number of collisions on a board
def num_collisions(board):
    n = len(board)
    num_pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if (board[i] == board[j]) or (abs(board[i] - board[j]) == abs(i - j)):
                num_pairs += 1
    return num_pairs

#print board
def print_board(board):
    n = len(board)
    for i in range(n):
        row = ['Q' if j == board[i] else '.' for j in range(n)]
        print(" ".join(row))


def hill_climbing(n):
    
    #Get initial chess board and the number of collisions per board
    current_board = create_board(n)
    current_collisions = num_collisions(current_board)

    #while loop is checking if your board has no more collisions
    while True:
        if current_collisions == 0:
            return current_board
        

        next_board = current_board[:]
        min_collisions = current_collisions
        prev_collisions = current_collisions

        #select random row to be modified
        row_change = random.randint(0, n-1)

        #go through each column, and change column of current queen to that column
        for col in range(n):
            if current_board[row_change] != col:
                next_board[row_change] = col
                new_collisions = num_collisions(next_board)

                #check if the collisions decreased, if so, set new value of min collisions to that number of collisions, and set current board to the new board found
                if new_collisions < min_collisions:
                    min_collisions = new_collisions
                    current_board = next_board[:]

        current_collisions = min_collisions

        #if there was no better solution found, restart recursively
        if (current_collisions == prev_collisions):
            return hill_climbing(n)
        

if __name__ == "__main__":
    n = 8
    result = hill_climbing(n)
    if result:
        print_board(result)
    else:
        print("no sln found")
        
