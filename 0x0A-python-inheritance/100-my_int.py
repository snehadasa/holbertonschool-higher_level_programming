#!/usr/bin/python3
"""
    module that inherits from int
    This is an example of test overriden methods(__eq__(==), __ne__(!=))
"""
class MyInt(int):
    """MyInt is a rebel which has '==' and '!=' inverted"""


    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
