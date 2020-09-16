#!/usr/bin/python3
"""
sends a POST request to a url with an email
"""


import urllib.request as request
import urllib.parse as parse
import sys


if __name__ == "__main__":
    data = parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
    with request.urlopen(sys.argv[1], data) as url_request:
        print(url_request.read().decode('utf-8'))
