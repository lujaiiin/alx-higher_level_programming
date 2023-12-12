#!/usr/bin/python3
"""Module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """inital"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """prop"""

        return self.__width

    @width.setter
    def width(self, value):
        """setter"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """prop"""

        return self.__height

    @height.setter
    def height(self, value):
        """setter"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """pro"""

        return self.__x

    @x.setter
    def x(self, value):
        """setter"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y pro"""

        return self.__y

    @y.setter
    def y(self, value):
        """setter"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates the rea of the rect"""
        return self.__width * self.__height

    def display(self):
        """prints shape out of #'s"""
        print('\n' * self.__y, end='')
        for i in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """sre"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width,self.height)

    def update(self, *args, **kwargs):
        """update fun"""

        if args is not None and len(args) != 0:
            k = len(args)
            if k >= 1:
                self.id = args[0]
            if k >= 2:
                self.width = args[1]
            if k >= 3:
                self.height = args[2]
            if k >= 4:
                self.x = args[3]
            if k >= 5:
                self.y = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """dectonary"""

        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x,
                "y": self.y}
