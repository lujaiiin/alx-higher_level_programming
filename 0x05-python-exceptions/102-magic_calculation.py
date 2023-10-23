#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > 0:
                raise Exception('Too far')
            else:
                result += (a + b) ** i / i
        except:
            result += a + b
            break
    return result
