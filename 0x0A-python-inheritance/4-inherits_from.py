#!/usr/bin/python3
"""
Returns true if object is an instance of a class that
inherited from specified class
"""


def inherits_from(obj, a_class):
    """ Return True if so and False Otherwise """
    return isinstance(obj, a_class)
