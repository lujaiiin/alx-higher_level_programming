#!/usr/bin/python3
"""Modules"""


def append_after(filename="", search_string="", new_string=""):
    """function"""
    with open(filename, 'r') as fi:
        liste = []
        while True:
            fo = fi.readline()
            if fo == "":
                break
            liste.append(fo)
            if search_string in fo:
                liste.append(new_string)
    with open(filename, "w") as lo:
        lo.writelines(liste)
