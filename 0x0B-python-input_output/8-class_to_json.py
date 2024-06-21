#!/usr/bin/python3
'''
Module for a function returning a dictionary description
with simple data structure for JSON serialization of an object.
'''


def class_to_json(obj):
    '''
    Module for a function returning a dictionary description
    with simple data structure for JSON serialization of an object
    '''

    return obj.__dict__
