#!/usr/bin/python3
"""Defines a class Square with a size, a position and a print method."""


class Square:
    """Defines a square by its private size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square.

        Args:
            size: the size of the square (an integer >= 0).
            position: a tuple of 2 positive integers, used to indent
                and offset the square when it is printed.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Gets or sets the position of the square.

        Raises:
            TypeError: if the position is not a tuple of 2 positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character # at its position.

        Prints an empty line if the size is 0.
        """
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
