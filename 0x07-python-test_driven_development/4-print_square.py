#!/usr/bin/python3
"""Module to print square pattern"""


def print_square(size):
    """prints square pattern for given size.

    size: size of the square to be printed.

    Return: square pattern.

    Raise: TypeError, ValueError.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
