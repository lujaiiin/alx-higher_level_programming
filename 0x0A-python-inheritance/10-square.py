#!/usr/bin/python3
"""Module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square"""

    def __init__(self, size):
        """func"""

        super().__init__(size, size)
        self.__size = size
