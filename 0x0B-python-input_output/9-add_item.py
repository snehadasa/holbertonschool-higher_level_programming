#!/usr/bin/python3
"""module to load, add and save arguments to a text file"""


import sys

save_7 = __import__("7-save_to_json_file").save_to_json_file
load_8 = __import__("8-load_from_json_file").load_from_json_file

try:
	f = load_8("add_item.json")
except:
	with open("add_item.json", "w"):
		myFile = []
		save_7(myFile, "add_item.json")
		f = load_8("add_item.json")

if len(sys.argv) < 2:
	pass
else:
	myFile = []
	myFile = load_8("add_item.json")
	myFile.extend(sys.argv[1:])
	save_7(myFile, "add_item.json")
