#!/usr/bin/python3
"""
geometry
"""


class BaseGeometry:
    """ Does calculations """
    def area(self):
        """ area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ checks integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""
Rectangle Class
"""


class Rectangle(BaseGeometry):
    """ Rectangle Class """
    def __init__(self, width, height):
        """ width and height """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)
