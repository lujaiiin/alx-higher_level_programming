#!/usr/bin/python3
"""
class Regtangle
"""


class Rectangle:
    """Rectangle class to de."""

    def __init__(self, width=0, height=0):
        """init function."""
        self.width = width
        self.height = height

    @property 
    def width(self):
        """geteer for private."""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for private."""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """getter for private."""
        return self.__height

    @height.setter
    def height(self, value):
        """seteer for private."""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
