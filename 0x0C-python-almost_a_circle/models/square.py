#!/usr/bin/python3
"""Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """init"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str"""

        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size"""

        return self.width

    @size.setter
    def size(self, value):
        """setter"""

        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """update"""

        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """update"""

        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """dict"""

        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
