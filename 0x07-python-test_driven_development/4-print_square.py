#!/usr/bin/python3
# 4-print_square.py
"""Defines a function that prints a square with the character #"""


def print_square(size):
    """Prints a square of character #

    Args:
        size(int): Dimensions of the square(l,w)
    Raises:
        ValueError: if size =< 0
        TypeError: if input size is not an int/number
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
