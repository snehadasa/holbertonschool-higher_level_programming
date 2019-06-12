#!/usr/bin/python3
"""module for unittest"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_square(unittest.TestCase):

    def test_id(self):
        """test for id"""

        b1 = Base(1)
        self.assertEqual(b1.id, 1)

        b2 = Base(2)
        self.assertEqual(b2.id, 2)

    def test_for_0(self):
        """test for 0 base"""

        b3 = Base(0)
        self.assertEqual(b3.id, 0)

    def test_for_higher_base(self):
        """test for higher value"""

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_for_string(self):
        """test for string"""

        b5 = Base("holberton")
        self.assertEqual(b5.id, "holberton")

    def test_for_decimal(self):
        """test for decimal base"""

        b6 = Base(3.5)
        self.assertEqual(b6.id, 3.5)

    def test_for_negative(self):
        """test for negative base"""

        b7 = Base(-8)
        self.assertEqual(b7.id, -8)

    def test_type_instance(self):
        """test for type and instance"""

        b9 = Base()
        self.assertTrue(isinstance(b9, Base))
        self.assertEqual(type(b9), Base)

    def test_tojsonstring_int(self):
        """tests for error messages of json string"""

        with self.assertRaises(TypeError) as f:
            Base.to_json_string(19)
        self.assertEqual("list_dictionaries must be a list of dictionaries",
                         str(f.exception))

    def test_tojsonstring_string(self):
        """tests for error messages of json string"""

        with self.assertRaises(TypeError) as f:
            Base.to_json_string("holberton")
        self.assertEqual("list_dictionaries must be a list of dictionaries",
                         str(f.exception))

    def test_tojsonstring_invalid_list(self):
        """tests for error messages of json string"""

        with self.assertRaises(TypeError) as f:
            Base.to_json_string([1, 2, 4, 7])
        self.assertEqual("list_dictionaries must be a list of dictionaries",
                         str(f.exception))

    def test_tojsonstring_set(self):
        """tests for error messages of json string"""

        with self.assertRaises(TypeError) as f:
            Base.to_json_string({1, 2})
        self.assertEqual("list_dictionaries must be a list of dictionaries",
                         str(f.exception))

    def test_tojsonstring_valid_dict(self):
        """test for valid dict"""

        dic = {'x': 3, 'y': 7, 'width': 11}
        json_dictionary = Base.to_json_string([dic])
        self.assertTrue(isinstance(dic, dict))
        self.assertTrue(isinstance(json_dictionary, str))
        self.assertEqual(json_dictionary, '[{"x": 3, "y": 7, "width": 11}]')

    def test_savetofile_valid(self):
        """test for valid save to file"""

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        res = ('[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},' +
               ' {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]')
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), len(res))

    if __name__ == "__main__":
        unittest.main()
