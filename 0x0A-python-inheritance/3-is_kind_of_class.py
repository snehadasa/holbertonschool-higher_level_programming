#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
        is_kind_of_class - module to check, object is instance of the class
        @obj: object
        @a_class: class
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
