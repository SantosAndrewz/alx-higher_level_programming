#!/usr/bin/python3
'''
Module checks if the object is exactly the instance of a given class.
'''


def is_same_class(obj, a_class):
    '''
    Function checks if objevt is exactly an instance of the given class.

    Args:
        obj: object to be checked.
        a_class: class to compare against.

    Returns:
        True if the object is exactly the instance of the given class,
        otherwise False.
    '''

    return type(obj) is a_class
