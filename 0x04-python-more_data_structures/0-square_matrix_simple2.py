#!/usr/bin/python3
def square_matrix_simple2(matrix=[]):
    return list(map(lambda row: list(map(lambda number: number**2, row)), matrix))
