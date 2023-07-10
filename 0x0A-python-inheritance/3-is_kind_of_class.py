#!/usr/bin/python3
"""Defines object is an instance of a class that inherited from"""
def is_kind_of_class(obj, a_class):
    """Checks for inheritance

    Args:
        obj (any)
        a_class (type)

    Returns:
        True if confirmed
        else False
    """
    if isinstance(obj, a_class):
        return True
    return False
