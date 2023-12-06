#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return dict(map(lambda xy: (xy[0], xy[1] * 2), a_dictionary.items()))
