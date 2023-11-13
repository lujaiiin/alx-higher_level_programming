#!/usr/bin/python3
"""Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructior"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter"""
        return self.width

    @size.setter
    def size(self, value):
        """setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """returns the obj"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """update attrs"""
        if args is not None and len(args) != 0:
            a = len(args)
            if a >= 1:
                self.id = args[0]
            if a >= 2:
                self.size = args[1]
            if a >= 3:
                self.x = args[2]
            if a >= 4:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns dict"""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
