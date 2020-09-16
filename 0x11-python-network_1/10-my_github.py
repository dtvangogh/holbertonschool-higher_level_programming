#!/usr/bin/python3
"""
Takes Github credentials and displays the user id #
"""

import requests
from sys import argv


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]

    request = requests.get('https://api.github.com/user',
                           auth=(username, password))
    if request.status_code != 200:
        print("None")
    else:
        json_dict = request.json()
        print(json_dict['id'])
