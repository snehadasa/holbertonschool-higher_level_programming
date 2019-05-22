#!/usr/bin/python3
class Square():
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size
            self._Square__position = position

    def area(self):
        return self._Square__size ** 2

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = value

    def my_print(self):
        if self.size == 0:
            print("")
            return
        for i in range(self.position[1]):
            print("")
        for i in range(self.size):
            for j in range(self.position[0]):
                print(" ", end="")
            for k in range(self.size):
                print("#", end="")
            print("")

    @property
    def position(self):
        return self._Square__position

    @position.setter
    def position(self, value):
        if value != tuple or value[0] != int or value[1] != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._Square__position = value
