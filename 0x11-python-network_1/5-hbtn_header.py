#!/usr/bin/python3
"""
prints the value of the X-Request-Id of the response header
"""
import requests
import sys


if __name__ == "__main__":
    request = requests.get(sys.argv[1])
    print(request.headers.get('X-Request-Id'))
