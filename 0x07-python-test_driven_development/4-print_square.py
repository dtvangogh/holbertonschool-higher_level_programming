#!/usr/bin/python3
"""
  Prints a square of #
"""


def print_square(size):
    """
      print square func
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0:
        raise ValueError("size must be >= 0")
    for y in range(size):
        for x in range(size):
            print("#", end="")
        print("")
