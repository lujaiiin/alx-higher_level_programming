#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    i = 0
    for i in my_list:
        if i == idx:
            return my_list[i]
    if idx > i:
        return None
