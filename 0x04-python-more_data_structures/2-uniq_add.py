#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_int = set()
    for x in my_list:
        unique_int.add(x)
    return sum(unique_int)
