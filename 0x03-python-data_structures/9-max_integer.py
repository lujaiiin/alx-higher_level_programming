#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        sume = 0
        for i in my_list:
            if (i > sume):
                sume = i
    elif len(my_list) == 0:
        sume = None
    return sume
