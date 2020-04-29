#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 1:
        char = 32
    else:
        char = 0
    print("{}".format(chr(i - char)), end='')
