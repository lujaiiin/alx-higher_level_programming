#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return list(map(lambda c: list(map(lambda e: e**2, c)), matrix))
