#!/usr/bin/python3
'''
Module for a function printing a text with 2 new lines after each of the
characters ., ? and:
'''


def text_indentation(text):
    '''
    Function printing a text with 2 new lines after characters: ., ? and :

    Args:
        text (str): text to be formated.

    Raises:
        TypeError: Raised when text is not a string.
    '''

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    charset = ['.', '?', ':']
    pr = ''
    x = 0

    while x < len(text):
        pr += text[x]
        if text[x] in charset:
            pr += '\n\n'
            while x + 1 < len(text) and text[x + 1] == ' ':
                x += 1
        x += 1
    print(pr.strip())
