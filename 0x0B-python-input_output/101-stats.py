#!/usr/bin/python3
"""Modules"""


def print_stats(size, status_codes):
    """function"""
    print("File size: {}".format(size))
    for i in sorted(status_codes):
        print("{}: {}".format(i, status_codes[i]))

if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    va = ['200', '301', '400', '401', '403', '404', '405', '500']
    c = 0

    try:
        for lin in sys.stdin:
            if c == 10:
                print_stats(size, status_codes)
                c = 1
            else:
                c += 1
            lin = lin.split()
            try:
                size += int(lin[-1])
            except (IndexError, ValueError):
                pass
            try:
                if lin[-2] in va:
                    if status_codes.get(lin[-2], -1) == -1:
                        status_codes[lin[-2]] = 1
                    else:
                        status_codes[lin[-2]] += 1
            except IndexError:
                pass
        print_stats(size, status_codes)
    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
