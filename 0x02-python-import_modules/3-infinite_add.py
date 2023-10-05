#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argl = len(sys.argv)
    res = 0
    if argl == 1:
        print(0)
    else:
        for i in range(1, argl):
            res = res +  int(sys.argv[i])
        print("{}".format(res))
