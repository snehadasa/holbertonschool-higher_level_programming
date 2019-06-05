#!/usr/bin/python3
"""module for looking an obj"""


def lookup(obj):
    """
        lookup - looks for available attributes and returns them.
        @obj: object
    """
    return dir(obj)
