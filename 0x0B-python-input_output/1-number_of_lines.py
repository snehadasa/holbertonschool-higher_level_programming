#!/usr/bin/python3
"""module to return number of lines"""


def number_of_lines(filename=""):
    i = 0
    with open(filename, encoding='utf-8') as myFile:
        for s in myFile:
            i += 1
    return i
