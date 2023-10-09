#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    first = tuple_a[0] if len(tuple_a) > 0 else 0
    sec = tuple_a[1] if len(tuple_a) > 1 else 0
    firb = tuple_b[0] if len(tuple_b) > 0 else 0
    secb = tuple_b[1] if len(tuple_b) > 1 else 0
    return first + firb, sec + secb
