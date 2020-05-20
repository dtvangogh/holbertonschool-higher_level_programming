#!/usr/bin/python3


"""square class"""


class Square:
    """
    Square
    """
    def __init__(self, size=0, position=(0,0)):
        """
        creates square
        """
        self.__size = size
        self.position = position
        if type(position[0]) is not int or type(position[1]) is not int:
            raise(TypeError("position must be a tuple of 2 positive integers"))

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
            for y in range(0, self.position[1]):
                print('')
            for y in range(self.__size):
                for x in range(0, self.position[0]):
                    print(' ', end='')
                for x in range(self.__size):
                    print("#", end="")
                print("")

    @property
    def position(self):
        """ position getter """
        return self.__position


    @position.setter
    def position(self, value):
        """ sets the position and error checking """
        s = "position must be a tuple of 2 positive integers"
        if type(value) is tuple:
            if len(value) != 2:
                raise TypeError(s)
            else:
                for i in range(len(value)):
                    if value[i] < 0:
                        raise TypeError(s)
            self.__position = value
        else:
            raise TypeError(s)
