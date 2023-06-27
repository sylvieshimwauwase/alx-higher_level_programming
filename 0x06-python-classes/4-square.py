#!/usr/bin/python3
"""Representing square"""


class Square:
    """Square class representation
    Attributes:
        __size (int): size of square
    """

    def __init__(self, size=0):
        """new instances of class square

        Args:
            size (int, optional): size of the square (default 0)

        Raises:
            TypeError: if size is integer
            ValueError: if size is less than 0
        """
        self.__size = size

    def size(self):
        """
        Getter for retrieving size of square
        Returns:
            int: size of square
        """
        return sef.__size

    def size(self, value):
        """
        Setter property for setting size of square

        Args:
            value (int): size of square

        Raises:
            TypeError: if size is an integer
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

        def area(self):
            """
            Calculates and returns area of square

            Returns:
                int: area of the square
            """
            return self.__size ** 2
