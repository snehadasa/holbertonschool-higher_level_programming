#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Tests maximum integer"""

    def test_self(self):
        lst = [1, 2, 7, 5, 9]
        result = max_integer(lst)
        self.assertEqual(result, 9)

    def test_empty(self):
        lst = []
        result = max_integer(lst)
        self.assertEqual(result, None)

    def test_for_negative_num(self):
        lst = [-9, -7, -6, -4]
        result = max_integer(lst)
        self.assertEqual(result, -4)

    def test_positive_float(self):
        lst = [3.5, 4.5, 0.4, 2.5]
        result = max_integer(lst)
        self.assertEqual(result, 4.5)
    
    def test_negative_float(self):
        lst = [-9.5, -7.5, -6.4, -2.3, -4.3]
        result = max_integer(lst)
        self.assertEqual(result, -2.3)
    
    def test_same_num(self):
        lst = [5, 5, 5, 5, 5, 5]
        result = max_integer(lst)
        self.assertEqual(result, 5)

    def test_float_and_int(self):
        lst = [-9, 7.5, 5.4, -6]
        result = max_integer(lst)
        self.assertEqual(result, 7.5)
    
    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)
