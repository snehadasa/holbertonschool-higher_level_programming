#!/usr/bin/python3
"""module to create a class called student"""


class Student():
	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	def to_json(self):
		if type(attrs) == list:
			func = self.__dict__.copy()
			for key in list(f.keys()):
				if key not in attrs:
del func[key]
return 
