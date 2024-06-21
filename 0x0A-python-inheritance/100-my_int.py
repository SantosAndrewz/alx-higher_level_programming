#!/usr/bin/python3
'''
Module for a class MyInt that inherits from int
'''


class MyInt(int):
    ''' Class inverts int operators == and != '''

    def __eq__(self, int_value):
        ''' Overridess == with behviours of != '''
        return (self.real != int_value)

    def __ne__(self, int_value):
        ''' Overrises != with behaviours of == '''

        return (self.real == int_value)
