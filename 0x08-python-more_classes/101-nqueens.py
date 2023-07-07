#!/usr/bin/python3
""" chess game"""


import sys


def solve_nqueens(n):
    """
    Solve the N Queens problem and print every possible solution.

    Args:
        n (int): The number of queens and the size of the chessboard.

    Raises:
        ValueError: If n is not an integer or smaller than 4.

    Prints:
        Every possible solution to the N Queens problem, with one solution.
    """
    if not isinstance(n, int):
        raise ValueError("N must be a number")
    if n < 4:
        raise ValueError("N must be at least 4")

    def is_safe(board, row, col):
        """
        Check if it's safe to place a queen on the chessboard.

        Args:
            board (list): The chessboard configuration.
            row (int): The row index.
            col (int): The column index.

        Returns:
            bool: True if it's safe to place a queen, False otherwise.
        """
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True

    def solve_util(board, col):
        """
        Recursive utility function to solve the N Queens problem.

        Args:
            board (list): The current chessboard configuration.
            col (int): The current column index to place a queen.

        Prints:
            The solutions to the N Queens problem.
        """
        if col == n:
            print_solution(board)
            return True
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                solve_util(board, col + 1)
                board[i][col] = 0

    def print_solution(board):
        """
        Print the current chessboard configuration.

        Args:
            board (list): The current chessboard configuration.
        """
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=" ")
            print()

    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_util(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    solve_nqueens(N)
