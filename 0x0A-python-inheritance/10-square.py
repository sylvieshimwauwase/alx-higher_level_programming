#!/usr/bin/python3
"""representing full rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """
        Initialize a Square object with the given size.

        Args:
        - size (int): The size of the square.
        """

        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

