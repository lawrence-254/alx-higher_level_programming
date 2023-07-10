#!/usr/bin/python3
"""Defines object used for checking inheritance"""


def inherits_from(obj, a_class):
    """Checks for inheritance

    Args:
        obj (any)
        a_class (type)

    Returns:
        True if inherited
        else False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
