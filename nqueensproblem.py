import random

def generate_random_board(n):
    return [random.randint(0, n-1) for _ in range(n)]

def calculate_attacking_pairs(board):
    n = len(board)
    attacking_pairs = 0

    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                attacking_pairs += 1

    return attacking_pairs

def hill_climbing(n, max_iterations=10000):
    current_board = generate_random_board(n)
    current_attacking_pairs = calculate_attacking_pairs(current_board)

    for _ in range(max_iterations):
        if current_attacking_pairs == 0:
            return current_board  # Solution found

        next_board = current_board.copy()
        row_to_change = random.randint(0, n-1)
        min_attacking_pairs = current_attacking_pairs

        for col in range(n):
            if current_board[row_to_change] != col:
                next_board[row_to_change] = col
                new_attacking_pairs = calculate_attacking_pairs(next_board)

                if new_attacking_pairs < min_attacking_pairs:
                    min_attacking_pairs = new_attacking_pairs
                    current_board = next_board.copy()

        current_attacking_pairs = min_attacking_pairs

    return None  # No solution found within max_iterations

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