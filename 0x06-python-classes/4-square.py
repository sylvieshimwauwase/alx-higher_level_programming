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
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Retrieving size of square"""
        return self.__size

    @size.setter
    def size(self, value):
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
