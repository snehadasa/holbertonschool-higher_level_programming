#!/usr/bin/python3
"""module to create an object from jason file"""


def load_from_json_file(filename):
	import json
	with open(filename, "r") as myFile:
		s = myFile.read()
		return json.loads(s)
