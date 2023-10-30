#!/usr/bin/python3
"""Module."""

def add_integer(a, b=98):
    """add function to add a + b"""

    if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')
    if type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')
    c = a + b
    c = int(c)
    return c
