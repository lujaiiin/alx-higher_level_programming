#!/usr/bin/python3
import sys as ll

def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as s:
        ll.stderr.write("Exception: {}\n".format(s))
        return None
