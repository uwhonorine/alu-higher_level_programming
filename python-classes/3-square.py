#!/usr/bin/python3
"""Defines a class Square with a validated size and an area method."""


class Square:
    """Defines a square by its private size."""

    def __init__(self, size=0):
        """Initializes a square.

        Args:
            size: the size of the square (an integer >= 0).

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current area of the square."""
        return self.__size ** 2
