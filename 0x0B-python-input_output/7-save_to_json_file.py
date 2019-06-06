#!/usr/bin/python3
"""module to write an object to a text file"""


def save_to_json_file(my_obj, filename):
    import json
    with open(filename, "w") as myFile:
        return json.dump(my_obj, myFile)
