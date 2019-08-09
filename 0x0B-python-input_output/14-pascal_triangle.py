#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return ""
<<<<<<< HEAD
=======

>>>>>>> df05daeb7b7fcfb5d52ad97d8f9fdc93265d0e90
    result = [[1]]
    for i in range(1, n):
        temp = [1]
        prev_result = result[i - 1]
        for j in range(1, i):
            temp.append(prev_result[j] + prev_result[j - 1])
        temp.append(1)
        result.append(temp)
    return result
