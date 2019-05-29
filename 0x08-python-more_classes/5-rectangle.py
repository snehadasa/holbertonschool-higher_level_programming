#!/usr/bin/python3
"""Rectangle class that defines a rectangle
with variables width and height"""

class Rectangle():
    """contains area, perimeters, __del__, __str__ & __repr__(object),
     getters & setters.initialize private variables."""
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return self.__width * 2 + self.__height * 2
    
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def __str__(self):
        rec = ""
        if self.__width == 0 or self.__height == 0:
            return rec
        for i in range(self.height):
            for j in range(self.width):
                rec += "#"
            rec += '\n'
        return rec[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
