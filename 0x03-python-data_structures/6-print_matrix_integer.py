#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        l = 0
        for i in matrix:
            for j in i:
                l = l + 1
                if l == len(i):
                    print(j, end = "")
                else:
                    print(j, end = " ")
            l = 0
            print()
