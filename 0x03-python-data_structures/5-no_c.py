#!/usr/bin/python3

def no_c(my_string):
    kk = ""
    for i in my_string:
        if i.upper() != 'C' or i.lower() != 'c':
            kk += i
    return kk
