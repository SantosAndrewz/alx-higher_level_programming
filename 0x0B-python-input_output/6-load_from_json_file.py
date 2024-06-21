#!/usr/bin/python3
'''
Module for a function creating an Object from a JSON file.
'''

import json


def load_from_json_file(filename):
    ''' Function creating an Object from a "JSON file" '''

    with open(filename, 'r', encoding='utf-8') as fn:
        return (json.load(fn))
