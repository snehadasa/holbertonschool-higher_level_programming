#!/usr/bin/python3
"""module Rectangle that inherits from base"""

from models.base import Base


class Rectangle(Base):
    """class Rectangle that has width and height."""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print("", end=" ")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                 self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        if len(args) != 0 and args:
            if (len(args) > 0):
                self.id = args[0]
            if (len(args) > 1):
                self.__width = args[1]
            if (len(args) > 2):
                self.__height = args[2]
            if (len(args) > 3):
                self.__x = args[3]
            if (len(args) > 4):
                self.__y = args[4]
            return
        for key in kwargs:
            if key is "id":
                self.id = kwargs["id"]
            if key is "width":
                self.__width = kwargs["width"]
            if key is "height":
                self.__height = kwargs["height"]
            if key is "x":
                self.__x = kwargs["x"]
            if key is "y":
                self.__y = kwargs["y"]

    def to_dictionary(self):
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
