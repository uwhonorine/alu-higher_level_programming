#!/usr/bin/python3
"""Defines a class Rectangle with a validated width and height."""


class Rectangle:
    """Defines a rectangle by its private width and height."""

    def __init__(self, width=0, height=0):
        """Initializes a rectangle.

        Args:
            width: the width of the rectangle (an integer >= 0).
            height: the height of the rectangle (an integer >= 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets or sets the width of the rectangle.

        Raises:
            TypeError: if the width is not an integer.
            ValueError: if the width is less than 0.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets or sets the height of the rectangle.

        Raises:
            TypeError: if the height is not an integer.
            ValueError: if the height is less than 0.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
