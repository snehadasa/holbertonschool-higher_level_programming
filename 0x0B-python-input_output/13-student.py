#!/usr/bin/python3
"""module to create a class called student"""


class Student():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) != list:
            return self.__dict__
        result = {}
        for i in attrs:
            if i in self.__dict__:
                result[i] = self.__dict__[i]
        return result

    def reload_from_json(self, json):
        for i in json:
            if i in self.__dict__:
                self.__dict__[i] = json[i]
