#!/usr/bin/python3
"""Function to check size of square"""


def print_square(size):
    """
    prints a square with the character '#'.

    Args:
        size (int): The size length of teh square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        TypeError: If size is a float and is less than 0.

        Returns:
            None
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
