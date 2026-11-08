#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle defined by a private width and a private height."""

    def __init__(self, width, height):
        """Initializes a rectangle.

        Args:
            width: the width of the rectangle (a positive integer).
            height: the height of the rectangle (a positive integer).
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
