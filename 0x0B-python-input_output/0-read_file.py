#!/usr/bin/python3
"""module to read and print the contents to stdout"""
def read_file(filename=""):
    with open(filename, encoding='utf-8') as myFile:
        s = myFile.read()
    print(s, end="")
