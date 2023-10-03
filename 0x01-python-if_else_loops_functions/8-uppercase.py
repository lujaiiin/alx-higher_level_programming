#!/usr/bin/python3
def uppercase(str):
    for i in str:
        lent = ord(i)
        if lent <= 122 and lent >= 97:
            lent = lent - 32
        print("{}".format(chr(lent)), end='')
    print()
