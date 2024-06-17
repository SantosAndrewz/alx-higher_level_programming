#!/usr/bin/python3
'''
Module for a locked class
'''


class LockedClass:
    ''' creates a locked class accepting only attribute 'first_name'.'''

    __slots__ = ['first_name']
