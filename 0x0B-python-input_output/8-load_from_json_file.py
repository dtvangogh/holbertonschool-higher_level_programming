#!/usr/bin/python3
""" Object from JSON file"""
import json


def load_from_json_file(filename):
    """object form Json file"""
    with open(filename, mode='r') as f:
        return json.load(f)
