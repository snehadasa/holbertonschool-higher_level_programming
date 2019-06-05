#!/usr/bin/python3
class MyList(list):
    """module that inherits from list
    subclass(MyList) of super class(list)"""

    def print_sorted(self):
        """print the list in sorted order"""
        print(sorted(self))
