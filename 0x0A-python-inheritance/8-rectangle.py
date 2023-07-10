#!/usr/bin/python3
"""Defines inherited class from 7-base_geometry.py."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines class with inheritance"""

    def __init__(self, width, height):
        """New instance of rectangle

        Args:
            width (int)
            height (int)
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
