#!/usr/bin/python3
"""representing full rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """
        Initialize a Square object with the given size.

        Args:
        - size: The size of the square.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than or equal to 0.
        """

        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Return the square description.

        Returns:
        - A string representing the square description.
        """

        return f"[Square] {self.__size}/{self.__size}"
