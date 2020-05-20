#!/usr/bin/python3
"""
 Square Class
"""


class Square:
    """ class Square """

    def __init__(self, size=0):
        """set size and create square instance"""
        if size < 0:
            raise ValueError('size must be >= 0')
        if type(size) is not int:
            raise TypeError("size must be an integer")
        self.__size = size
