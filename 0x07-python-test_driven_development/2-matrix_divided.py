#!/usr/bin/python3
"""matrix"""


def matrix_divided(matrix, div):
    """ divide all elements of a matrix by int"""

    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(error)
    for line in matrix:
        if not isinstance(line, list):
            raise TypeError(error)
    for row in matrix:
        if len(row) == 0:
            raise TypeError(error)
        if len(row) == len(matrix[0]):
                pass
        else:
                raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[0 for length in range(3)] for length in range(3)]
    newmatrix = [[round(length / div, 2) for length in row] for row in matrix]
    return newmatrix


