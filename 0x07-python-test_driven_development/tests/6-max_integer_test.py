#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ the unit testing class"""

    def test1(self):
        """test with all numbers"""
        max_integer([1, 2, 3, 4]) == 4
        max_integer([1, 3, 4, 2]) == 4

    def test_values(self):
        """checking for bad values"""
        self.assertRaises(TypeError, max_integer, 7)
        self.assertRaises(TypeError, max_integer, None)

    def test_str(self):
        """checks failure if apssed string """
        max_integer("hi") == 'i'
        self.assertRaises(TypeError, max_integer, [1, 2, 3, "hi"])

    def test_empty(self):
        """ checks for no arguments"""
        self.assertEqual(max_integer([]), None)

    def test2(self):
        """ checks placement of max """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([10, 10, 10, 10]), 10)
