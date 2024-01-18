#!/usr/bin/python3
"""Creates and defines a class Square."""


class Square:
    """Creates a class - Square."""

    def __init__(self, size=0):
        """Initializing a class Square.

        Args:
            size(int): Shows the size of the Square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
