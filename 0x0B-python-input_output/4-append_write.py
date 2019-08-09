#!/usr/bin/python3
"""module to write a append to a text file and return number of
characters written"""


def append_write(filename="", text=""):
    with open(filename, mode='a', encoding='utf-8') as myFile:
        s = myFile.write(text)
        return s
