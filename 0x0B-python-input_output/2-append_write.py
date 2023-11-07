#!/usr/bin/python3
"""Module"""


def append_write(filename="", text=""):
    """function"""

    with open(filename, "a+") as f:
        li = f.write(text)
        return li
