#!/usr/bin/python3
'''
Module for the function returning the list of available attributes and methods
'''


def lookup(obj):
    '''
    Function returning a list of available object attributes and methods.

    Args:
        obj: The object whose list is to be returned.

    Returns:
        A list of attributesn and methods of the object.
    '''

    return dir(obj)
