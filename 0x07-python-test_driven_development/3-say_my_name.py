#!/usr/bin/python3
'''
The module prints my name.
'''


def say_my_name(first_name, last_name=""):
    '''
    Function prints My name is <first name> <last name>

    Args:
        first_name (str): First name to be printed.
        last_name (str): Last name to be printed.

    Raises:
        TypeError: If the names entered are not of the type string.
    '''

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name).strip())
