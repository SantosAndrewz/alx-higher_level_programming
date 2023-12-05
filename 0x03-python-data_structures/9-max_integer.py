#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        my_newlist = sorted(my_list, reverse=True)
        return (my_newlist[0])
