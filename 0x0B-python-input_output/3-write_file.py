#!/usr/bin/python3
"""module to write a string to a text file and return number of
characters written"""


def write_file(filename="", text=""):
    with open(filename, mode='w', encoding='utf-8') as myFile:
        s = myFile.write(text)
        return s
