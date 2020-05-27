#!/usr/bin/python3
"""
Locked Class
"""


class LockedClass:
    """
    prevent user making new instance attributes
    """
    __slots__ = ['first_name']

    def __init__(self, firstname=""):
        self.first_name = firstname
