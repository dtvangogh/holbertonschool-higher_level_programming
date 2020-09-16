#!/usr/bin/python3
"""
use the package requests to fetch url and print body text and type
"""


import requests


request = requests.get('https://intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(request.text)))
print("\t- content: {}".format(request.text))
