#!/usr/bin/python3
"""module for base class"""

import json


class Base():
    """Base class"""

    __nd_objects = 0
    def __init__(self, id=None):
        """initialising base"""
        if id is not None:
            self.id = id
        else:
            Base.__nd_objects += 1
            self.id = Base.__nd_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if type(list_dictionaries) != list:
            raise TypeError("list_dictionaries must be a list")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open(str(cls.__name__) + ".json", "w+") as myFile:
            if list_objs is None:
                myFile.write(Base.to_json_string([]))
                return
            if type(list_objs) != list and list_objs is not None:
                raise TypeError("list_objs must be a list")
            l = []
            for base_obj in list_objs:
                l.append(base_obj.to_dictionary())
            return myFile.write(Base.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        l = []
        if json_string is None or json_string == []:
            return l
        l.append(json_strin)
        return l
