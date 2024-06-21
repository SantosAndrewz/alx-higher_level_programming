#!/usr/bin/python3
'''
Module for a function returning the JSON representation of an object(str).
'''

import json


def to_json_string(my_obj):
    ''' Function that returns the JSON representation of anobject(str) '''

    return json.dumps(my_obj)
