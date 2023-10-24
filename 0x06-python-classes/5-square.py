#!/usr/bin/python3
"""Module."""


class Square:
    """Square class."""

    def __init__(self, size=0):
        """Initialz."""
        self.size = size

    @property
    def size(self):
        """to retrieve it"""
        self.__size = size

    @size.setter
    def size(self, value):
        """ to set it."""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """area."""
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
