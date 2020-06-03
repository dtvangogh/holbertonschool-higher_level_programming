#!/usr/bin/python3
"""
JSON to Object
"""
import json


def from_json_string(my_str):
    """ returns an object represented by jason string"""
    return json.loads(my_str)
