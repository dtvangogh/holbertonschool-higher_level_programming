#!/usr/bin/python3
""" pascals triangle method """


def pascal_triangle(n):
    """ returns a list of numbers, n is which num to go up to"""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    oldlist = [[1], [1, 1]]
    m = n - 1
    previous_list = [1, 1, 1]
    for x in range(2, n):
        newlist = [1 for i in range(0, n - m + 2)]
        for y in range(1, n - m + 1):
            newlist[y] = previous_list[0 + y - 1] + previous_list[1 + y - 1]
        previous_list = newlist
        oldlist.append(newlist)
        m = m - 1

    return oldlist
