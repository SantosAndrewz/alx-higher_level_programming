#!/usr/bin/python3
''' Module for a fumction adding a new attribute to an object if possible '''


def add_attribute(obj, name, value):
    ''' Function adds a new attribute to an object if possible. '''

    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
