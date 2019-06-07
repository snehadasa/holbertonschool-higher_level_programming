#!/usr/bin/python3
"""module to return dict description with simple data structure"""


def class_to_json(obj):
	return obj.__dict__
