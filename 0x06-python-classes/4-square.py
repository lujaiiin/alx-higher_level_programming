#!/usr/bin/python3
"""Module."""


class Square:
    """Square class."""

    def __init__(self, size=0):
        """Initialaiz."""
        self.size = size

    @property
    def size(self):
        """to retrieve it."""
        return self.__size

    @size.setter
    def size(self, value):
        """to set it."""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area."""
        return self.__size * self.__size
