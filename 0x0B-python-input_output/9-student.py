#!/usr/bin/python3
'''
Module for a class Student that defines a student.
'''


class Student:
    '''
    Creates a class Student defined by their first name, last name and age.
    '''
    def __init__(self, first_name, last_name, age):
        ''' Method initializing a new student instance. '''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        ''' Method returns a dictionary representaion of a student instance '''

        return self.__dict__
