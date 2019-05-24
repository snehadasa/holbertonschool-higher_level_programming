#!/usr/bin/python3
def matrix_divided(matrix, div):
    new[] = 0
    for i in matrix:
        if matrix[i] != int or matrix[i] != float:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats"))
        elif div != int or div != float:
            raise TypeError("div must be a number")
        elif div == 0:
            raise ZeroDivisionError("division by zero")
        elif
            raise TypeError("Each row of the matrix must have the same size")
        else:
            new[] = matrix / div
    return new
