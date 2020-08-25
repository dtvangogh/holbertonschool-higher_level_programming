#!/usr/bin/python3
"""
sends a POST request to the url as argv1 and email as argv2
"""
import requests
import sys


if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    request = requests.post(sys.argv[1], email)
    print(request.text)
