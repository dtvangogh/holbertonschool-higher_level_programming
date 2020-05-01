#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_arg = len(argv)
    if num_arg == 1:
        print("{} arguments.".format(num_arg - 1))
    elif num_arg == 2:
        print("{} argument:".format(num_arg - 1))
    else:
        print("{} arguments:".format(num_arg - 1))
    for i in range(num_arg):
        if i == 0:
            continue
        print("{}: {}".format(i, argv[i]))
