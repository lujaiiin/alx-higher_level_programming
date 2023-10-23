#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as s:
        sys.stderr.write("Exception: {}\n".format(s))
        return None
