#!/usr/bin/python3
"""module for unittest"""

import unittest
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_rectangle(unittest.TestCase):

    def test_for_instances(self):
        """test for instances"""

        r1 = Square(5)

    def test_for_string(self):
        """test for string"""

        with self.assertRaises(TypeError):
            r1 = Square("holberton")

    def test_for_decimal(self):
        """test for decimal one argument"""

        with self.assertRaises(TypeError):
            r1 = Square("3.6")

    def test_for_negative(self):
        """test for negative """

        with self.assertRaises(ValueError):
            r1 = Square(-7, -1)

    def test_valid_arguments(self):
        """test for valid arguments"""

        r1 = Square(1, 2, 3, 4)

    def test_passing_more_args(self):
        """tests for passing more arguments"""

        with self.assertRaises(TypeError):
            r1 = Square(1, 2, 3, 4, 5, 6, 7, 8)

    def test_no_arguments(self):
        """tests for passing no arguments"""

        with self.assertRaises(TypeError):
            r1 = Square()

    def test_for_unknown_args(self):
        """tests for passing unknown argument"""

        with self.assertRaises(NameError):
            r1 = Square(holberton)

    def test_for_floats(self):
        """tests for error messages of json string"""

        with self.assertRaises(TypeError):
            r1 = Square(1.3, 6.8, 7, 9)

    def test_passing_none(self):
        """test for passing none for arguments"""

        with self.assertRaises(TypeError):
            r1 = Square(None)

    def test_for_valid_display(self):
        """test for valid display"""

        r1 = Square(2, 3, 2, 2)

    if __name__ == "__main__":
        unittest.main()
