#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry:
    """Defining class BaseGeometry """

    def area(self):
        """area of the BaseGeometry """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validating parameter as an integer
        Args:
            name (str): name of parameter.
            value (int): parameter to validate.
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is <= 0.
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
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