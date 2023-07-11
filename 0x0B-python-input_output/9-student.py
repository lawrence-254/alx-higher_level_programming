#!/usr/bin/python3
"""Defines a class object student."""


class Student:
    """Class object student."""

    def __init__(self, first_name, last_name, age):
        """Initializes student.

        Args:
            first_name (str)
            last_name (str)
            age (int)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get sudent dictionary."""
        return self.__dict__
