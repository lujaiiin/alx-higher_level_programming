#!/usr/bin/python3
import calculator_1 as ff
import sys
if __name__ == "__main__":
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    f = int(sys.argv[1])
    s = sys.argv[2]
    t = int(sys.argv[3])
    if s == "+":
        print("{} + {} = {}".format(f, t, ff.add(f, t)))
    elif s == "*":
        print("{} * {} = {}".format(f, t, ff.mul(f, t)))
    elif s == "-":
        print("{} - {} = {}".format(f, t, ff.sub(f, t)))
    elif s == "/":
        print("{} / {} = {}".format(f, t, ff.div(f, t)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
