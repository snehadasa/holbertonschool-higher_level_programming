#!/usr/bin/python3
class MyList(list):
    """module that inherits from list
    subclass(MyList) of super class(list)"""


    def __init__(self):
        """initialisation"""
        list.__init__(self)

    def print_sorted(self):
        """print the list in sorted order"""
        print(sorted(self))
