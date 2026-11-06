#!/usr/bin/python3
"""Defines a class Square with a size property and an area method."""


class Square:
    """Defines a square by its private size."""

    def __init__(self, size=0):
        """Initializes a square.

        Args:
            size: the size of the square (an integer >= 0).
        """
        self.size = size

    @property
    def size(self):
        """Gets or sets the size of the square.

        Raises:
            TypeError: if the size is not an integer.
            ValueError: if the size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size ** 2
