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

    def update(self, *args, **kwargs):
        """Updates the square
        """

        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                    self.height = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
                if i == 4:
                    self.y = args[4]
                if i == 5:
                    self.y = args[5]

        else:
            if len(kwargs) > 0:
                keys = kwargs.keys()
                for i in keys:
                    if i == 'id':
                        self.id = kwargs['id']
                    if i == 'size':
                        self.width = kwargs['size']
                        self.height = kwargs['size']
                    if i == 'x':
                        self.x = kwargs['x']
                    if i == 'y':
                        self.y = kwargs['y']

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
