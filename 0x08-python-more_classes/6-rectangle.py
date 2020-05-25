#!/usr/bin/python3
"""
Rectangle
"""


class Rectangle:
    """ Rectangle Class """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ initializes the wid and height of rec """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ get the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ get the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ find the area of the rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ find the perimeter of the rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """printing rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for height in range(self.__height):
            for width in range(self.__width):
                rectangle += "#"
            if height is not self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """ string representation of an instance of a square """
        width = str(self.__width)
        height = str(self.__height)
        return "Rectangle(" + width + ", " + height + ")"

    def __del__(self):
        """ delete message """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
