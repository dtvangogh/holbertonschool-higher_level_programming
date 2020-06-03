#!/usr/bin/python3
"""
Writes File
"""


def write_file(filename="", text=""):
    """ writes to file """
    with open(filename, mode='w', encoding='utf-8') as f:
        a = f.write(text)
    return a
