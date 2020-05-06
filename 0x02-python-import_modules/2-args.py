#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    number_of_arguments = len(argv)
    if number_of_arguments == 1:
        print("{} arguments.".format(number_of_arguments - 1))
    elif number_of_arguments == 2:
        print("{} argument:".format(number_of_arguments - 1))
    else:
        print("{} arguments:".format(number_of_arguments - 1))
    for i in range(number_of_arguments):
        if i == 0:
            continue
        print("{}: {}".format(i, argv[i]))
