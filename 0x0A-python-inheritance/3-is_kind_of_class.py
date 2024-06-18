#!/usr/bin/python3
'''
Module checks if object is an isntance of or if the object is an instance
of a class that inherited from the specified class.
'''


def is_kind_of_class(obj, a_class):
    '''
    Function  checks if object is an instance of or if the object is an
    instance of a class that inherited from the specified class.

    Args:
        obj: object to check.
        a_class: class to compare against.

    Returns:
        True if the object is an instance of, or if the object is an instance
        of a class that inherited from, the specified class; otherwise False.
    '''

    return isinstance(obj, a_class)
