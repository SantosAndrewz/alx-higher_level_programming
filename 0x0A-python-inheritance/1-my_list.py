#!/usr/bin/python3
'''
Module for a class myList that inherits from list:
'''


class MyList(list):
    ''' class inheriting from class list '''
    def print_sorted(self):
        '''
        Method prints list list in ascending order.
        Assumes all elements are of the same type int
        '''

        sorted_list = sorted(self)
        print(sorted_list)
