#!/usr/bin/python3
"""
Reads the file
"""


def read_file(filename=""):
    """  reads a text file and prints file """
    with open(filename, encoding='utf-8') as f:
        print(f.read())
