#!/usr/bin/python3
"""
displays X-Request ID
"""


import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as request:
        r = request.headers
    print(r['X-Request-Id'])
