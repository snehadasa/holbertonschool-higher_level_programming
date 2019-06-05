#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
        is_same_class - module to check for object if is instance of the class
        @obj: object
        @a_class: class
    """

    if isinstance(type(obj), a_class):
        return True
    else:
        return False
