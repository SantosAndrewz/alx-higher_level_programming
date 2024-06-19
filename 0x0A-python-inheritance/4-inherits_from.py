#!/usr/bin/python3
'''
Module checks if the object is an instance of a class that is inherited
directly or indirectly from the specified class
'''


def inherits_from(obj, a_class):
    '''
    Function checks if the object is an instance of a class that is inherited
    directly or indirectly from the specified class

    Args:
        obj: object to be checked
        a_class: class to compare against.

    Returns:
        True if the object is an instance of a class that inherited that
        specified class, otherwise False.
    '''

    return isinstance(obj, a_class) and type(obj) is not a_class
