#!/usr/bin/python3
def uppercase(str):
    for i in str:
        l = ord(i)
        if l <= 122 and l >= 97:
            l = l - 32
        print("{}".format(chr(l)), end='')
    print()
