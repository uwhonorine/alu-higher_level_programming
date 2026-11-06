#!/usr/bin/python3
"""Defines a class Square with a private size."""


class Square:
    """Defines a square by its private size."""

    def __init__(self, size):
        """Initializes a square.

        Args:
            size: the size of the square (not verified).
        """
        self.__size = size
