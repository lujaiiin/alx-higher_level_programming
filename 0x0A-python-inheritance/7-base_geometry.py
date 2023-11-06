#!/usr/bin/python3
"""Module"""


class BaseGeometry:
    """classy"""

    def area(self):
        """la function"""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """int fun"""

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
