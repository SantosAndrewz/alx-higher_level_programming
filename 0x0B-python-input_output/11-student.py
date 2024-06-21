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

    def to_json(self, attrs=None):
        ''' Method returns a dictionary representaion of a student instance '''

        if attrs is not None:
            if all(isinstance(attr, str) for attr in attrs):
                return {attr: getattr(self, attr) for attr
                        in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        '''
        Method replaces all attributes of the Student
        instance with the provided dictionary.
        '''

        for key, value in json.items():
            setattr(self, key, value)
