#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) <= ord('z') and ord(str[i]) >= ord('a'):
            char = chr(ord(str[i]) - 32)
        else:
            char = chr(ord(str[i]))
        print("{:s}".format(char), end="")
    print("")
