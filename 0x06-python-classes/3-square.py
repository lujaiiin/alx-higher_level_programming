#!/usr/bin/python3
"""Module."""


class Square:
    """Square Class, areas."""

    def __init__(self, size=0):
        """Initialize."""
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Area of square."""
        return self.__size * self.__size
