#!/usr/bin/python3
"""Square representation"""


class Square:
    """Representing Square"""

    def __init__(self, size=0):
        """Initializing square class
        Args:
            size: size of square
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an intger")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
