#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    li = list(map(lambda i: list(map(lambda x: x**2, i)), matrix))
    return li
