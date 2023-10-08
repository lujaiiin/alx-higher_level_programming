#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        l = 0
        for j in i:
            l = l + 1
            if l == len(i):
                print("{:d}".format(j), end='')
            else:
                print("{:d}".format(j), end=' ')
        print()
