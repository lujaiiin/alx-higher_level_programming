#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        li = (sum(i * j for i, j in my_list) / sum(j for i, j in my_list))
        return li
    else:
        return 0
