#!/usr/bin/python3
"""Function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor

    Args:
        matrix (list): a list of lists representing matrix
        div (int 0r float): the divisor

    Returns:
        list: a new matrix with elements divided by div

    Raises:
        TypeError: If a matrix is not a valid matrix of integers/float
        ZeroDivisionError: If div is equal to zero
    """

    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    div_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return div_matrix
