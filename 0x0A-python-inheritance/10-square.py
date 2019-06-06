#!/usr/bin/python3
"""
    module to create an BaseGeometry class.
    with public instances area and integer validator.
"""


class BaseGeometry():
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """value validator"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
        subclass of the super class BaseGeometry
        which contains width and height as private instance attributes.
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of the class rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns a string"""
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """
        subclass Square that inherits from Rectangle.
        has private attribute size(all sides are equal)
    """

    def __init__(self, size):
        """instantiation of size"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns area of the square"""
        return self.__size ** 2
