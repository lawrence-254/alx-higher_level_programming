#!/usr/bin/python3
# 0-add_integer.py
"""
    A function that adds two integers
"""


def add_integer(a, b=98):
    """Add two integers and return the result

    Cast a and b to integers if they are floats

    Raises:
        TypeError: when a or b are not integers and floats
    """

    """ Check if a is an integer or float"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    """Check if b is an integer or float"""
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    """Cast a and b to integers if they are floats"""
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    """Add the integers and return the result"""
    return int(a + b)
