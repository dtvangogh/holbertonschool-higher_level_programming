#!/usr/bin/python3
"""Student class"""


class Student:

    """The Student class"""

    def __init__(self, first_name, last_name, age):
        """Instantiation function for Student class
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of init
        """

        if not isinstance(attrs, list):
            return self.__dict__
        for var in attrs:
            if not isinstance(var, str):
                return self.__dict__
        string_dict = {}
        for string in attrs:
            if string in self.__dict__.keys():
                string_dict[string] = self.__dict__[string]
        return string_dict


    def reload_from_json(self, json):
        """ reloads from json"""
        for item in json:
            setattr(self, item, json[item])
