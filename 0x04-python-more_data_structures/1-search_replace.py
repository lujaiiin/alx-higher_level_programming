#!/usr/bin/python3
def search_replace(my_list, search, replace):
    li = map(lambda va : replace if va == search else va, my_list)
    li = list(li)
    return li
