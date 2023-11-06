#!/usr/bin/python3
"""Mudules"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rec class inhert a base class"""

    def __init__(self, width, height):
        """init function"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
