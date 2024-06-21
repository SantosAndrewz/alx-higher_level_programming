#!/usr/bin/python3
'''
Module for writing an object to a text file, using a JSON representation.
'''

import json


def save_to_json_file(my_obj, filename):
    '''
    Function writes an Object to a text file, using a JSON representation
    '''

    with open(filename, 'w', encoding='utf-8') as fn:
        json.dump(my_obj, fn)
