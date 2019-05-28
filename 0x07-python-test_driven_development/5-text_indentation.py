#!/usr/bin/python3
"""Module to print the text given seperated by delimeters."""


def trim_spaces(string):
    """function to trim spaces.

    string: string where the spaces are to be trimmed.

    Return: new string
    """

    i = 0
    for j in range(len(string)):
        if string[j] == " ":
            i = i+1
        else:
            break
    print(string[i:], end="")


def text_indentation(text):
    """function to print indented text seperated by delimeters.

    text: text to be printed.

    Return: text after indentation

    Raises: TypeError
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    lst = text.replace('.', '.@#$').replace(
            '?', '?@#$').replace(':', ':@#$').split('@#$')
    for st in lst[:-1]:
        trim_spaces(st)
        print("")
        print("")
    trim_spaces(lst[-1])
