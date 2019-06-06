#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str:
        return 0
    dic = {'M': 1000, 'C': 100, 'X': 10, 'I': 1, 'V': 5, 'L': 50, 'D': 500}
    total = 0
    for i in reversed(roman_string):
        if total <= 5 * num:
            num -= num
            total += num
    return total
