#!/usr/bin/python3
"""Module for add_integer"""


def add_integer(a, b=98):
    """ adds integer

    a: first integer
    b: second integer

    Errors: TypeError if either of the args are ints or floats.

    Returns: Sum of two integers
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
