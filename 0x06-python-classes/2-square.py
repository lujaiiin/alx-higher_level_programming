#!/usr/bin/python3
"""Module."""


class Square:
    """Square Class, define"""

    def __init__(self, size=0):
        """ Initial.

        Args:
            size: int."""
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
