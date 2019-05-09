#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[pow(x, 2) for x in col] for col in matrix]
