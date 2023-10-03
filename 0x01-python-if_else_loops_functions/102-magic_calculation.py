#!/usr/bin/python3
def magic_calculation(a, b, c):
    if c > b:
        sume = a + b
    elif b > a:
        sume = c
    else:
        sume = a * b - c
    return sume
