#!/usr/bin/python3
"""Modules"""
import json


def load_from_json_file(filename):
    """function"""

    with open(filename, "r") as fi:
        return json.loads(fi.read())
