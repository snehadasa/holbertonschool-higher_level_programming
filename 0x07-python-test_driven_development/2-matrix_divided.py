#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix"
                        "(list of lists) of integers/floats")
    new = []
    for i in matrix:
        temp = []
        if not isinstance(i, list):
            raise TypeError("matrix must be a matrix"
                            "(list of lists) of integers/floats")
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError("matrix must be a matrix"
                                "(list of lists) of integers/floats")
            temp.append(round(j / float(div), 2))
        new.append(temp)
    return new
