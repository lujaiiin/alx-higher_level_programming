#!/usr/bin/python3
import sys
if __name__ == "__main__":
    al = len(sys.argv)
    res = 0
    if al == 1:
        print(0)
    else:
        for i in range(1, al):
            res = res +  int(sys.argv[i])
        print("{}".format(res))
