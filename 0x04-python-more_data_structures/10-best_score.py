#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    i = None
    j = 0
    for x, y in a_dictionary.items():
        if y > j:
            j = y
            i = x
    return i
