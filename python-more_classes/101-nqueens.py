#!/usr/bin/python3
"""
N Queens Problem Solver
Solves the N queens puzzle using backtracking algorithm
"""

import sys


def is_safe(board, row, col, n):
    """Check if placing a queen at board[row][col] is safe"""
    # Check this column on upper rows
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper diagonal on left side
    for i in range(row - 1, -1, -1):
        j = col - (row - i)
        if j >= 0 and board[i] == j:
            return False

    # Check upper diagonal on right side
    for i in range(row - 1, -1, -1):
        j = col + (row - i)
        if j < n and board[i] == j:
            return False

    return True


def solve_nqueens(n, row, board, solutions):
    """Solve N Queens problem using backtracking"""
    if row == n:
        # Found a solution, add it to solutions list
        solution = []
        for i in range(n):
            solution.append([i, board[i]])
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)


def main():
    """Main function to handle input and solve N Queens problem"""
    # Check number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize board and solutions list
    board = [-1] * n
    solutions = []

    # Solve the N Queens problem
    solve_nqueens(n, 0, board, solutions)

    # Print all solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
