#!/usr/bin/python3
"""Modules"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """initial"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """function 2"""

        return self.__dict__
