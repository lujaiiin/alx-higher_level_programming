#!/usr/bin/python3
"""Module"""


def write_file(filename="", text=""):
    """function"""

    with open(filename, "w+") as f:
        li = f.write(text)
        return li
