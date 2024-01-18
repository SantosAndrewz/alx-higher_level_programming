#!/usr/bin/python3
"""Creates and defines a class Square."""


class Square:
    """Creates a class - Square."""

    def __init__(self, size=0):
        """Initializing a class Square.

        Args:
            size(int): Shows the size of the Square.
        """
        self.size = size

    @property
    def size(self):
        """Getting the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setting the size of the square to value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        area_t = self.__size * self.__size
        return (area_t)
