#!/usr/bin/python3
"""module to return number of lines"""


def number_of_lines(filename=""):
    with open(filename) as myFile:
        for i, l in enumerate(myFile):
            pass
    return i + 1
