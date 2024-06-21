#!/usr/bin/python3
'''
Module for appending a string at the end of a text file.
Returns the number of characters added.
'''


def append_write(filename="", text=""):
    '''
    Function appends a string at the end of a text file(UTF8) and
    returns the numbers of characters added
    '''

    with open(filename, 'a', encoding='utf-8') as fn:
        return (fn.write(text))
