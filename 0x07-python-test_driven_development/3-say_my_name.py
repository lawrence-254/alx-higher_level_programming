#!/usr/bin/python3
# 3-say_my_name.py
"""A function that prints first name and last name"""


def say_my_name(first_name, last_name=""):
    """Print fullname

    Args:
        first_name(str): prints the first name as string
        last_name(str): prints a last name as a string
    Raises:
        TypeError: if the input is not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
