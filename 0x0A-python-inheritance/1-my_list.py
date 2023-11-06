#!/usr/bin/python3
"""Module"""


class MyList(list):
    """MyList class"""

    def print_sorted(self):
        """print metod"""
        li = self[:]
        li = sorted(li)
        print(li)
