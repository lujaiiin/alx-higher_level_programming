#!/usr/bin/python3
"""Module."""

def print_square(size):
    """print function to print square"""

    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) == float and size < 0:
        raise TypeError('size must be an integer')
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
