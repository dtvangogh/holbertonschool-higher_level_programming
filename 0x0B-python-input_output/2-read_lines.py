#!/usr/bin/python3
"""
Read certain amount of lines
"""


def read_lines(filename="", nb_lines=0):
    """ Read n lines of file """
    count = 0
    with open(filename, encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end='')
        for line in f:
            if count < nb_lines:
                print(line, end='')
                count += 1
