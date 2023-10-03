#!/usr/bin/python
def uppercase(str):
    for i in str:
        l = ord(i)
        if l <= 122 and l >= 97:
            l = l - 32
            print("{}".format(chr(l)), end='')
        else:
            print("{}".format(chr(l)), end='')
    print()
