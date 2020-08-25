#!/usr/bin/python3
"""
prints response from url passed as argv(1)
"""
import urllib.request as request
import urllib.error as error
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as request:
            print(request.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
