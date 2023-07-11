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

    def to_json(self, attrs=None):
        """Get sudent dictionary.

        Args:
            attrs (list)
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Change all the attributes of parent class student.

        Args:
            json (dict)
        """
        for k, v in json.items():
            setattr(self, k, v)
