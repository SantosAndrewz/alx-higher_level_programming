#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_squared = []
    for row in matrix:
        matrix_squared.append([x**2 for x in row])
    return matrix_squared
