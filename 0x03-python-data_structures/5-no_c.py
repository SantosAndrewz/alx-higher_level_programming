#!/usr/bin/python3
def no_c(my_string):
    my_newstring = ""
    for x in my_string:
        if x != 'c' and x != 'C':
            my_newstring += x
    return my_newstring
