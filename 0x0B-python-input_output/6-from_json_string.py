#!/usr/bin/python3
"""module to convert string to object using JSON encoder"""


def from_json_string(my_str):
    import json
    return json.loads(my_str)
