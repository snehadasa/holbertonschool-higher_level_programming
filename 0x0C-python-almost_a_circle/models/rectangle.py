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
        """width property"""

        return self.__width

    @width.setter
    def width(self, value):
        """property setter"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height property"""

        return self.__height

    @height.setter
    def height(self, value):
        """property setter"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x property"""

        return self.__x

    @x.setter
    def x(self, value):
        """property setter"""

        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y property"""

        return self.__y

    @y.setter
    def y(self, value):
        """property setter"""

        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__y = value

    def area(self):
        """area contains
        width and height"""

        return self.__width * self.__height

    def display(self):
        """display the rectangle with the symbol #"""

        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print("", end=" ")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """str representation of rectangle"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """updating with args and kwargs.
        *args - all the arguments.
        **kwargs - entire dic"""

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
            if key == "id":
                self.id = kwargs["id"]
            if key == "width":
                self.__width = kwargs["width"]
            if key == "height":
                self.__height = kwargs["height"]
            if key == "x":
                self.__x = kwargs["x"]
            if key == "y":
                self.__y = kwargs["y"]

    def to_dictionary(self):
        """return dictionary representation"""

        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
