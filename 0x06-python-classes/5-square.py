#!/usr/bin/python3


"""square class"""


class Square:
    """
    Square
    """
    def __init__(self, size=0):
        """
        creates square
        """
        self.__size = size

    def area(self):

        """returns area of square"""

        return (self.__size ** 2)

    @property
    def size(self):

        """size getter"""

        return self.__size

    @size.setter
    def size(self, value):

        """sets size"""

        if type(value) is not int:
            raise(TypeError("size must be an integer"))
        if value < 0:
            raise(ValueError("size must be >= 0"))
        self.__size = value

    def my_print(self):
        """ printssquare """
        if self.size == 0:
            print("")
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print("")
