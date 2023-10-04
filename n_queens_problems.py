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

def hill_climbing(n, max_iterations=100000):
    current_board = create_board(n)
    current_attacking_pairs = attacking_pairs(current_board)

    #while loop is checking if your board is empty or not
    for _ in range(max_iterations):
        if current_attacking_pairs == 0:
            return current_board
        
        next_board = current_board.copy()
        row_to_change = random.randint(0, n-1)
        min_attacking_pairs = current_attacking_pairs
        prev_attacking_pairs = current_attacking_pairs

        for col in range(n):
            if current_board[row_to_change] != col:
                next_board[row_to_change] = col
                new_attacking_pairs = attacking_pairs(next_board)

                if new_attacking_pairs < min_attacking_pairs:
                    min_attacking_pairs = new_attacking_pairs
                    current_board = next_board.copy()

        current_attacking_pairs = min_attacking_pairs
        if (current_attacking_pairs == prev_attacking_pairs):
            return hill_climbing(n, max_iterations)
        
def print_board(board):
    n = len(board)
    for i in range(n):
        row = ['Q' if j == board[i] else '.' for j in range(n)]
        print(" ".join(row))
    print()

if __name__ == "__main__":
    n = 8  # Change 'n' to the desired board size
    solution = hill_climbing(n)

    if solution:
        print(f"Solution for {n}-Queens:")
        print_board(solution)
    else:
        print(f"No solution found for {n}-Queens within the maximum iterations.")

#go through each row
#try every possible column configuration for the queen
#see which one results in a lower number of collisions
#add them to a list of stuff to try out
#try a new board
        
