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
            raise TypeError("list_dictionaries must be a list of dictionaries")
        for k in list_dictionaries:
            if type(k) != dict:
                raise TypeError("list_dictionaries must be a"
                                " list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        res = []
        with open(str(cls.__name__) + ".json", "w+") as myFile:
            if list_objs is None:
                myFile.write(Base.to_json_string(res))
                return
            if type(list_objs) != list and list_objs is not None:
                raise TypeError("list_objs must be a list")
            for base_obj in list_objs:
                res.append(base_obj.to_dictionary())
            return myFile.write(Base.to_json_string(res))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string is "":
            return []
        if type(json_string) != str:
            raise TypeError("json_string must be a string")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy_instance = 0
        if (cls.__name__) is "Square":
            dummy_instance = cls(5)
        elif (cls.__name__) is "Rectangle":
            dummy_instance = cls(5, 8)
        else:
            raise TypeError("cls should be either Square or Rectangle")
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        res = []
        with open(str(cls.__name__) + ".json", "r") as myFile:
            list_obj = cls.from_json_string(myFile.read())
            for list_row in list_obj:
                res.append(cls.create(**list_row))
            return res
