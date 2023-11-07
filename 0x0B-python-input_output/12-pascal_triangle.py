#!/usr/bin/python3
"""Modules"""


def pascal_triangle(n):
    """function"""

    my = [[1]]
    if n <= 0:
        return []
    while len(my) in range(n):
        m = my[-1]
        me = [1]
        for j in range(len(m) - 1):
            me.append(m[j] + m[j + 1])
        me.append(1)
        my.append(me)
    return my
