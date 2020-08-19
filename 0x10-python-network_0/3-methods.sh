#!/bin/bash
# takes in a URL and displays all HTTP methods possible
curl -sI "$1" | grep "Allow:" | sed -ne 's/^Allow: //p'
