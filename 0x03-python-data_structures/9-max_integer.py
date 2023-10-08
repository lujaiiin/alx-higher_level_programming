#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        sume = 0
        for i in my_list:
            if (i > sume):
                sume = i
        return sume
