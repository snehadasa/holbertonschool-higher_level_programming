#!/usr/bin/python3
def remove_char_at(str, n):
    char = ""
    for i, c in enumerate(str):
        if i != n:
            char = char + c
    return char
