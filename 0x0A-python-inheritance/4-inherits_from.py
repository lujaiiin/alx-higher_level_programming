#!/usr/bin/python3
"""Module"""

def inherits_from(obj, a_class):
    """inhert fun"""

    if dir(obj) == dir(a_class) and isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
