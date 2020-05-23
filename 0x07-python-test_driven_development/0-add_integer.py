#!/usr/bin/python3
"""
 Return sum of a and b
 Converts float to integer
 Errors included
"""



def add_integer(a, b=98):
    """
     addition function
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
