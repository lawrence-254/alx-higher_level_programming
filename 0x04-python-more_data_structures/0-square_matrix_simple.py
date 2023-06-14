#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_1 = matrix.copy()

    for i in range(len(matrix)):
        matrix_1[i] = [x**2 for x in matrix[i]]

    return (matrix_1)
