#!/usr/bin/python3
def remove_Cc(my_string):
    new_string = ""
    for i in range(0, len(my_string)):
        if my_string[i] is not 'c' and my_string[i] is not 'C':
            new_string += my_string[i]
    return new_string
