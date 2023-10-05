#!/usr/bin/python3
import sys
if __name__ == "__main__":
    al = len(sys.argv)
    alli = 0
    if al == 1:
        print(0)
    else:
        for i in range(1, al):
            alli = alli +  int(sys.argv[i])
        print("{}".format(alli))
