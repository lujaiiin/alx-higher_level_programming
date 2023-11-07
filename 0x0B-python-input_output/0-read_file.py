#!/usr/bin/python3
"""Modules"""


def read_file(filename=""):
    """function read file"""

    with open(filename, 'r', encoding="utf-8") as l:
        print(l.read(), end='')
