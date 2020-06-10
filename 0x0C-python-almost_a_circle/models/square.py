#!/usr/bin/python3
"""Documentation for a Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):

    """Square Class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Square class
            size: the size of the square
            x: the x coordinate
            y: the y coordinate
            id: the id of the object
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Str Problem"""

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """Gets the size attribute
        """

        return self.width

    @size.setter
    def size(self, value):
        """Sets size attribute
        """

        self.width = value
        self.height = value
