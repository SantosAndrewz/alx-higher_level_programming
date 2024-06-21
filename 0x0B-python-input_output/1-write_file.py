#!/usr/bin/python3
'''
Module for a function writing a string to a text file and
returns number of characters written.
'''


def write_file(filename="", text=""):
    ''''
    function writes a string to a text file and
    returns the number of characters written.
    '''

    with open(filename, 'w+') as fn:
        return (fn.write(text))
