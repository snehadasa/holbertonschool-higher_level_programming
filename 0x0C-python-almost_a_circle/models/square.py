#!/usr/bin/python3
"""module that defines class Square that inherits fro class Rectangle"""


class Square(Rectangle):
    """class Square that inherits from subclass Rectangle. contains size"""

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                 self.x, self.y, self.width)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(size) != int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value
