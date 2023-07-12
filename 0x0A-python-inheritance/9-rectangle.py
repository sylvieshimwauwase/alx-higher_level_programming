#!/usr/bin/python3
"""representing full rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representing class defined using BaseGeometry"""

    def __init__(self, width, height):
        """
        initializing a rectangle object with given width and height
        Args:
            width: The width of the rectangle
            height: The height of the rectangle

        Raises:
            TypeError: if the width or height is not an integer
            ValueError: if width or height is less than or equal to 0
            """

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
        - The area of the rectangle.
        """

        return self.__width * self.__height

    def __str__(self):
        """
        Return the rectangle description.

        Returns:
        - A string representing the rectangle description.
        """

        return f"[Rectangle] {self.__width}/{self.__height}"
