#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str:
        return 0
    dic = {'M': 1000, 'C': 100, 'X': 10, 'I': 1, 'V': 5, 'L': 50, 'D': 500}
    dec = 0
    value_prev = dic.get(roman_string[0])
    for i in roman_string:
        if value_prev < dic.get(i):
            dec += dic.get(i) - value_prev * 2
        else:
            value_prev = dic.get(i)
            dec += dic.get(i)
    return dec
