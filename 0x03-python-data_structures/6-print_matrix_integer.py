#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for row in matrix:
        for i, x in enumerate(row):
            print("{:d}".format(x), end=" " if i != (len(row) - 1) else "")
        print()
