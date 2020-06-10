#!/usr/bin/python3
"""Rectangle Class"""


from models.base import Base


class Rectangle(Base):

    """Recangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation of Rectangle
        Arguments
            width: the width of rectangle
            height: the height of rectangle
            x: the x coord of rectangle
            y: the y coordd of rectangle
            id: the id of the rectangle
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the width
        """

        return self.__width

    def __str__(self):
        """Str problem"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def display(self):
        """Prints rectangle with #s
        """
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(' ', end="")
            for j in range(self.__width):
                print('#', end="")
            print()

    @width.setter
    def width(self, value):
        """Sets the width
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets height
        Returns:
            the height of the instance
        """

        return self.__height

    @height.setter
    def height(self, value):
        """Sets height
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets x attribute
        """

        return self.__x

    @x.setter
    def x(self, value):
        """Set x attribute
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets y attribute
        """

        return self.__y

    @y.setter
    def y(self, value):
        """Sets y attribute
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area of rectangle
        """

        return self.__width * self.__height

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

    def to_dictionary(self):
        """Returns a dictionary
        """

        dictionary = {}
        dictionary['id'] = self.id
        dictionary['x'] = self.x
        dictionary['y'] = self.y
        dictionary['width'] = self.width
        dictionary['height'] = self.height
        return dictionary
