#!/usr/bin/python3
"""
 add area of square
"""


class Square:
    """ Square """

    def __init__(self, size=0):
        """ initializes a square with attributes size/area """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
                raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ finds the area of a square """
        return (self.__size ** 2)
