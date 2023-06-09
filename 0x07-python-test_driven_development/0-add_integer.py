#!/usr/bin/python3
"""this module is of adding 2 integers"""


def add_integer(a, b=98):
    """Returning sum of two integers or float as integers
    Args:
        a: first argument
        b: second argument
    Returns:
        sum of arguments
    Raises:
        TypeError: if either of arguments not an integre or a float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
