#!/usr/bin/python3
"""module to add attribute if possible"""


def add_attribute(object, attr, val):
    """
        add attribute if possible.
        @object: some object
        @attr: attribute
        @val: value to be added
    """
    if not hasattr(object, "__slots__") and not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    if hasattr(object, "__slots__") and not hasattr(object, attr):
        raise TypeError("can't add new attribute")
    setattr(object, attr, val)
