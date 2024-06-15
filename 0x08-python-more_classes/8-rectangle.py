#!/usr/bin/python3
'''
Module for empty class Rectangle that defines a rectangle.
'''


class Rectangle:
    '''
    creates a Rectangle object.
    '''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''
        Initializes the new rectangle.

        Args:
            width (int): width of the new rectangle.
            height (int): height of the new rectangle.
        '''

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        ''' Gets the width of the rectangle. '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' Sets width of the rectangle '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''Gets the height of the rectangle. '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' Sets the height of the rectangle '''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        ''' Calculates the area of the rectangle '''
        return self.__width * self.__height

    def perimeter(self):
        ''' Calculates the perimeter of the rectangle. '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        '''
        Method returns a string representation of the rectangle with the
        character '#'.
        '''

        if self.__width == 0 or self.__height == 0:
            return ''
        sym = str(self.print_symbol)
        return '\n'.join([sym * self.__width for x in range(self.__height)])

    def __repr__(self):
        '''
        Method returns a string representation of the rectangle for
        recreation.
        '''
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        '''
        Method prints a message when the Rectangle instance is deleted.
        '''

        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''
        Method returns the bigger of the rectangles based on their areas.

        Args:
            rect_1 (Rectangle): first rectangle.
            rect_2 (Rectangle): second rectangle.

        Returns:
            Rectangle: the rectangle with the bigger area
                       or rect_1 if their areas are equal.
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
