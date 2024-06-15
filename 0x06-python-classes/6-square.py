#!/usr/bin/python3
"""Creates and defines a class Square."""


class Square:
    """Creates a class - Square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing a class Square.

        Args:
            size(int): Shows the size of the Square.
            position(int, int): the coordinates for the position of the square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getting the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setting the position of the square to value."""
        if not (isinstance(value, tuple) or len(value) != 2
                and not all(isinstance(n, int) for n in value)
                and not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square."""
        area_t = self.__size * self.__size
        return (area_t)

    def my_print(self):
        """Prints the square in the stdout with character #"""

        if self.__size == 0:
            print("")
            return

        for i in range(self.__position[1]):
            print("")

        for x in range(self.__size):
            print(" " * self.__position[0], end="")
            for y in range(self.__size):
                print("#", end="")
            print("")
