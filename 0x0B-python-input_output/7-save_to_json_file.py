#!/usr/bin/python3
"""
Save Object to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """ save to jason file """
    with open(filename, mode='w') as f:
        f.write(json.dumps(my_obj))
