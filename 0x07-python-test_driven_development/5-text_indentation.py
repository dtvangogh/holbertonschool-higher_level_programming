#!/usr/bin/python3
"""
 returns new lines after seperators
"""


def text_indentation(text):
    """
       Prints a new text with new indents
       text: text to manipulate
    """

    if not isinstance(text, str) or text is None or len(text) < 0:
        raise TypeError("text must be a string")
    i = 0
    for char in text:
        if char == '?' or char == '.' or char == ':':
            print(char, end="")
            print("")
            print("")
            i = 1
        else:
            if i == 0:
                print(char, end="")
            else:
                if char == ' ' or char == '\t':
                    pass
                else:
                    print(char, end="")
                    i = 0
