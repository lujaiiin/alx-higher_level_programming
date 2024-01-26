#!/usr/bin/python3
""" Modules """


def peak(n, s, e):
    """peak functions"""

    if s == e:
        return n[s]

    m = int((e - s) / 2) + s

    if n[m - 1] < n[m] and n[m + 1] < n[m]:
        return n[m]

    if n[m + 1] > n[m]:
        return peak(n, m + 1, e)

    return peak(n, s, m)

def find_peak(list_of_integers):
    """ find_peak function"""

    if list_of_integers is None or list_of_integers == []:
        return None

    return peak(list_of_integers, 0, len(list_of_integers) - 1)
