#!/usr/bin/python3
import sys
"""
Module
"""


def nad(li):
    """cal fun"""

    lib = []
    ary = []
    a = []
    i = 1
    aryy = []
    for j in range(li):
        y = j
        ary = []
        for l in range(li):
            if l != y and l != (li - i):
                a = [y, l]
                ary.append(a)
        aryy.append(ary)
        i += 1

    err = [j for s in aryy for j in s]
    j = 1

    for l in err:
        lib.append(l)
        j += 1
        if j == li + 1:
            print(lib)
            lib = []
    print(lib)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    nad(int(sys.argv[1]))
