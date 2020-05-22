#!/usr/bin/python3
"""
print whole name
"""


def say_my_name(first_name, last_name=""):
    """say my name func"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("{:s} {:s}".format(first_name, last_name))
