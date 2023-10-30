#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """Rectangle ll class"""
    def __init__(self, width=0, height=0):
        """intial fun"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """geter fun"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter fun"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """get fun"""
        return self.__height

    @height.setter
    def height(self, value):
        """ste fun"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """area fun"""
        return self.__width * self.__height

    def perimeter(self):
        """permieter fun"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """return prinsa"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for i in range(self.__height))
            return string
    def __repr__(self):
        """return ala"""
        return f"Rectangle({self.__width}, {self.__height})"
