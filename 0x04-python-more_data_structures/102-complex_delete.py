#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dict_keys = list(a_dictionary.keys())

    for searched_key in dict_keys:
        if a_dictionary[searched_key] == value:
            del a_dictionary[searched_key]
    return a_dictionary
