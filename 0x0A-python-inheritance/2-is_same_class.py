#!/usr/python3
"""Defines a class object"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class

    Args:
        obj (any)
        a_class (type)
    Returns:
        True if object is instance ofclass
        else False
        """
    if type(obj) == a_class:
        return True
    return False
