#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError("Cannot create new instance attributes")
        self.__dict__[name] = value
