#!/usr/bin/python3
"""Defines square from a rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Use rectangle to produce square."""

    def __init__(self, size):
        """Defines a square.

        Args:
            size (int)
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
