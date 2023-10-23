#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as d:
        sys.stderr.write("Exception: {}\n".format(d))
        return False
    except TypeError as x:
        sys.stderr.write("Exception: {}\n".format(x))
        return False
    else:
        return True
