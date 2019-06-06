#!/usr/bin/python3
"""module to return the JSON representation of an object"""


def to_json_string(my_obj):
    import json
    return json.dumps(my_obj)
