#!/usr/bin/python3
"""
Number of lines
"""


def number_of_lines(filename=""):
    """ counts number of lines """
    count = 0
    with open(filename) as f:
        for line in f:
            count += 1
    return count
