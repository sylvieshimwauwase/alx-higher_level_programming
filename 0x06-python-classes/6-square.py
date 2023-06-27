#!/usr/bin/python3
"""Representing square"""


class Square:
    """Square class representation
    Attributes:
        __size (int): size of square
        __position (tuple): position of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """new instances of class square

        Args:
            size (int, optional): size of the square (default 0)
            position (tuple, optional): position of the square (default (0,0))
        Raises:
            TypeError: if size is integer
            ValueError: if size is less than 0
            TypeError: if position is not a tuple of 2 positive integer
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieving the position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates and returns area of square

        Returns:
            int: area of the square
        """

        return self.__size ** 2

    def my_print(self):
        """
        prints square using '#' character
        if size is 0 prints an empty line
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
