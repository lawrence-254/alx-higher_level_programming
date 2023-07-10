#!/usr/bin/python3
"""Define a class MyInt that inherits from int."""


class MyInt(int):
    """Initialise myint"""

    def __ne__(self, value):
        """Changes != to =="""
        return self.real == value

    def __eq__(self, value):
        """Changes == to !="""
        return self.real != value
