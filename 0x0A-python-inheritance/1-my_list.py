#!/usr/bin/python3
""" the Mylist function """


class MyList(list):
    """the myList class """

    def print_sorted(self):
        """ print sorted list"""
        newlist = self
        newlist.sort()
        print(newlist)
