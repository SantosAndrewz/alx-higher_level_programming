#!/usr/bin/python3
'''
Module for a function that divides all elementsof a matrix
'''


def matrix_divided(matrix, div):
    '''
    Function divides a matrix

    Args:
        matrix (list): lists of lists of integers and/or floats.
        div (int/float): The divisor of the matrix.

    Raises:
        TypeError: If matrix is not a lists of integers and/or floats.
        TypeError: If rows of the matrix have different sizes.
        TypeError: If div is not a float or integer.
        ZeroDivisionError: If div is equal to 0.

    Return:
        List of lists of floats: each element divided by the div and rounded
                                 to decimal places,
    '''

    # Checks if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or any(not isinstance(row, list)
                                           for row in matrix):
        raise TypeError('matrix must be a matrix (list of lists) \
of integers/floats')
    if not matrix or any(not row for row in matrix):
        raise TypeError('matrix must be a matrix (list of lists) \
of integers/floats')
    if not all(all(isinstance(e, (int, float)) for e in row) for row
               in matrix):
        raise TypeError('matrix must be a matrix (list of lists) \
of integers/floats')
    # checks if each row in the matrix is the same size as the others.
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    # checks for type of div.
    if not isinstance(div, (int, float)) or div != div:
        raise TypeError('div must be a number')

    # Diviaor
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
