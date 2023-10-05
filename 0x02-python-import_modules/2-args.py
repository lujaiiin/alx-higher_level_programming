#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argl = len(sys.argv)
    if argl == 1:
        print("{} arguments.".format(argl - 1))
    elif argl == 2:
        print("{} argument:".format(argl - 1))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(argl - 1))
        for i in range(1, argl):
            print("{}: {}".format(i, sys.argv[i]))
