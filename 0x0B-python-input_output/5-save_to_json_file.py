#!/usr/bin/python3
"""Mudules"""
import json


def save_to_json_file(my_obj, filename):
    """functions"""
    with open(filename, "w+") as l:
        l.write(json.dumps(my_obj))
