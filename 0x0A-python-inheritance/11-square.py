#!/usr/bin/python3
'''
Module for a class Square which inherits from Rectangle.
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' Creating a class Square that inherits from class Rectangle '''

    def __init__(self, size):
        ''' initializes class Square and validates 'size' '''

        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        ''' a string representation of class square '''

        return (f'[Square] {self.__size}/{self.__size}')
