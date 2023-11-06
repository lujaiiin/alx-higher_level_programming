#!/usr/bin/python3
"""Module"""


def add_attribute(obj, key, value):
    """function add"""

    if hasattr(obj, "__dict__"):
        setattr(obj, key, value)
    else:
        raise TypeError("can't add new attribute")
