#!/usr/bin/python3
"""Modules"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """initial"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function 2"""

        try:
            for j in attrs:
                if type(j) != str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        li = dict()
        for i, v in self.__dict__.items():
            if i in attrs:
                li[i] = v
        return li
