#!/usr/bin/python3
"""Module."""

def matrix_divided(matrix, div):
    """matrix function"""
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    for i in matrix:
        if not isinstance(i, list) or len(i) == 0:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        return [[round(j / div, 2) for j in i] for i in matrix]
