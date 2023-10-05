#!/usr/bin/python3
import calculator_1 as ka
if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, ka.add(a, b)))
    print("{} - {} = {}".format(a, b, ka.sub(a, b)))
    print("{} * {} = {}".format(a, b, ka.mul(a, b)))
    print("{} / {} = {}".format(a, b, ka.div(a,b)))
