#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        lene = 0
        for j in i:
            lene = lene + 1
            if lene == len(i):
                print("{:d}".format(j), end='')
            else:
                print("{:d}".format(j), end=' ')
        print()
