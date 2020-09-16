#!/usr/bin/python3
"""
print Error code if the HTTP status >= 400
"""
import sys
import requests


if __name__ == "__main__":
    request = requests.get(sys.argv[1])
    if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)
