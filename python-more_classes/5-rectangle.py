#!/usr/bin/python3
"""Defines a class Rectangle that announces its own deletion."""


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

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle.

        The perimeter is 0 if the width or the height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns the rectangle drawn with the character #.

        Returns an empty string if the width or the height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        row = "#" * self.__width
        return "\n".join([row] * self.__height)

    def __repr__(self):
        """Returns a string that can recreate the rectangle with eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message when a rectangle is deleted."""
        print("Bye rectangle...")
