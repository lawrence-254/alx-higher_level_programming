#!/usr/python3
"""Class my list"""


class MyList(list):
    """Prints in ascending order"""
    def print_sorted(self):
        print(sorted(self))
