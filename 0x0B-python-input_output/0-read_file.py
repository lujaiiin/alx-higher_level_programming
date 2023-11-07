#!/usr/bin/python3
"""Modules"""


def read_file(filename=""):
    """function read file"""
    with open(filename, "r") as fil:
        print(fil.read(), end="")
