#!/usr/bin/python3
"""Module."""

class Square:
    """Square Class, areas."""

    def __init__(self, size=0):
        """Initials.

        Args:
            size: int"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """AREA of square.

        Args:
            size: int"""
        l = self.__size * self.__size
        return l
