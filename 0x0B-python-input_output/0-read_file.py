#!/usr/bin/python3
'''
Module for the function reading a text file(UTF8) and prints it to stdout
'''


def read_file(filename=""):
    ''' Function reading a text file(UTF8) and prints it to stdout '''

    with open(filename, 'r', encoding='utf-8') as fn:
        print(fn.read())
