#!/usr/bin/python3
"""module that defines class Square that inherits fro class Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from subclass Rectangle. contains size"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    @property
    def size(self):
        """size property"""

        return self.__size

    @size.setter
    def size(self, value):
        """property setter
        width, height size"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
        self.__size = value

    def update(self, *args, **kwargs):
        """updating with args and kwargs.
        *args - all the arguments.
        **kwargs - entire dic"""

        if args and len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
            return
        for key in kwargs:
            if key == "id":
                self.id = kwargs["id"]
            if key == "size":
                self.size = kwargs["size"]
            if key == "x":
                self.x = kwargs["x"]
            if key == "y":
                self.y = kwargs["y"]

    def to_dictionary(self):
        """return dictionary representation"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
