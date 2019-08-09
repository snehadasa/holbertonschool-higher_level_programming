#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return ""
    result = [[1]]
    for i in range(1, n):
        temp = [1]
        prev_result = result[i - 1]
        for j in range(1, i):
            temp.append(prev_result[j] + prev_result[j - 1])
        temp.append(1)
        result.append(temp)
    return result
