#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if my_list == 0:
        return None
    answer = my_list[0]
    for i in my_list:
        if i > answer:
            answer = i
    return answer
