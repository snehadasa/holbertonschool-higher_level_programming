#!/usr/bin/python3
"""module for base class"""


class Base():
    """Base class"""

    __nd_objects = 0
    def __init__(self, id=None):
        """initialising base"""
        if id is not None:
            self.id = id
        else:
            Base.__nd_objects += 1
            self.id = Base.__nd_objects
