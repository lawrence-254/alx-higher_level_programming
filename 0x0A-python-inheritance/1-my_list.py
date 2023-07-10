#!/usr/python3
"""Class my list"""


class MyList(list):
    """Implents function to print list in ascending order"""
    def print_sorted(self):
        """Print list in ascending order"""
        print(sorted(self))
