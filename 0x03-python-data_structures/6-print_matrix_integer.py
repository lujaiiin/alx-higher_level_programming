#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    l = 0
    for i in matrix:
        for j in i:
            l++
            if l == len(i):
                print("{:d}".format(j), end = "")
            else:
                print("{:d}".format(j), end = " ")
        l = 0
        print()
