#!/usr/bin/python3
import sys as ll


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as d:
        ll.stderr.write("Exception: {}\n".format(d))
        return False
    except TypeError as x:
        ll.stderr.write("Exception: {}\n".format(x))
        return False
