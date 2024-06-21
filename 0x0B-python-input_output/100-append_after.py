#!/usr/bin/python3
'''
Module inserts a line of text to a file, after each line containing
a specific string.
'''


def append_after(filename="", search_string="", new_string=""):
    '''
    Module inserts a line of text to a file, after each line containing
    a specific string.
    '''

    lines = []
    with open(filename, 'r') as fn:
        for line in fn:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, 'w') as fn:
        fn.writelines(lines)
