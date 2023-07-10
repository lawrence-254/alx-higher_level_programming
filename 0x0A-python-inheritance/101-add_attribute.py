#!/usr/bin/python3
"""Defines an object that adds attribute to objects."""


def add_attribute(obj, att, value):
    """Checks if attribute can be added and adds.

    Args:
        obj (any)
        att (str)
        value (any):
    Raises:
        TypeError: when attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
