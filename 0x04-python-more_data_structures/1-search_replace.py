#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_newlist = []
    for x in my_list:
        if x == search:
            my_newlist.append(replace)
        else:
            my_newlist.append(x)
    return my_newlist
