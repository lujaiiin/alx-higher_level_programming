#!/usr/bin/python3
"""Module"""
from models.base import Base


class Rectangle(Base):
    """rec"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """pr"""

        return self.__width

    @width.setter
    def width(self, value):
        """setter"""

        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """heght"""

        return self.__height

    @height.setter
    def height(self, value):
        """setter"""

        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """x pr"""

        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""

        self.val("x", value)
        self.__x = value

    @property
    def y(self):
        """y"""

        return self.__y

    @y.setter
    def y(self, value):
        """setter"""

        self.val("y", value)
        self.__y = value

    def val(self, name, value, eq=True):
        """val"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """area"""

        return self.width * self.height

    def display(self):
        """fun"""

        print('\n' * self.__y, end='')
        for i in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """sre"""

        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """update"""

        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """up"""

        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """dic"""

        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
