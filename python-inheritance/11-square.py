#!/usr/bin/python3
"""Defines a class Square with its own description."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square defined by a private size."""

    def __init__(self, size):
        """Initializes a square.

        Args:
            size: the size of the square (a positive integer).
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Returns the description: [Square] <width>/<height>."""
        return "[Square] {}/{}".format(self.__size, self.__size)
