#!/usr/bin/python3
def print_last_digit(number):
    lst = str(number)
    kel = len(lst)
    lst = lst[kel - 1]
    lst = int(lst)
    print(lst, end='')
    return (lst)
