#!/usr/bin/python3
def magic_calculation(a, b):
    import magic_calculation_102 as dd
    if b > a:
        d = dd.add(a, b)
        for j in range(4, 6):
            d = dd.add(d, j)
        return (d)
    else:
        return (dd.sub(a, b))
