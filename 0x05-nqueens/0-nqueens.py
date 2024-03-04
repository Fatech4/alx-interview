#!/usr/bin/python3
"""The N queens puzzle is the challenge of placing N non-attacking
queens on an N×N chessboard. Write a program that solves the N queens
problem."""
import sys


def is_safe(board, row, col):
    # Check if there is a queen in the same column or diagonal
    for i in range(row):
        if board[i][1] == col or \
           abs(board[i][0] - row) == abs(board[i][1] - col):
            return False
    return True


def solve_n_queens_util(board, row, N, solutions):
    if row == N:
        solutions.append(list(board))
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = (row, col)
            solve_n_queens_util(board, row + 1, N, solutions)
            board[row] = (-1, -1)


def solve_n_queens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_n_queens_util([(-1, -1)] * N, 0, N, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_n_queens(N)
