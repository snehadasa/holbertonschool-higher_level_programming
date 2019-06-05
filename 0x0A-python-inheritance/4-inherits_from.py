#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
        inherits_from - checks if obj is subclass of a_class
        @obj: object
        @a_class: class to check
    """

    if issubclass(type(obj), a_class) and not type(obj) == a_class:
        return True
    else:
        return False
