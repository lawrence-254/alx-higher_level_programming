#!/usr/bin/python3
"""
A function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number and return the result

    Args:
        div(float/it): denominator
        matrix(list): list containing int and/or floats

    Raises:
        ZeroError: if div == 0
        TypeError: matrix == NAN,
            div != int/float
            matrix.row1 >/< matrix.row2

    Returns: new matrix of dividends
    """

    """Check if matrix is a list of lists of integers or floats"""
    if not isinstance(matrix, list) or
    not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    """Check if div is a number (integer or float)"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    """Check if div is not equal to 0"""
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
