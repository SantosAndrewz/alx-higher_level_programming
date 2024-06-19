#!/usr/bin/python3
'''
Module for a class BaseGeometry.
'''


class BaseGeometry:
    ''' creates a class BaseGeometry '''

    def area(self):
        '''
        Public instance method that raises an Exception.

        Raises:
            Exception: display message 'area() is not implemented'.
        '''

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''
        Method that validates value.

        Args:
            name (str): name of the value.
            value (int): value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: If value is less than or equal to 0.
        '''

        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')

        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
