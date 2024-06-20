#!/usr/bin/python3
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


class Rectangle(BaseGeometry):
    ''' Creates a class Rectangle that inherits from class BaseGeometry '''

    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        ''' Calculates area of the rectangle. '''

        return self.__width * self.__height

    def __str__(self):
        ''' Returns a formatted string representation of the rectangle. '''

        return (f'[Rectangle] {self.__width}/{self.__height}')
