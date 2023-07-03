#!/usr/bin/python3
"""Defines a Rectangle with dimensions."""


class Rectangle:
    """A rectangle class."""

    def __init__(self, width=0, height=0):
        """Rectangle initialisation with dimension defined

        Args:
            width(int):width is the shortest side measurements of the rectacle
            height(int):the mesurement of the longer side
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """A get function for the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """A set function for the width property that ensures it is an int"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """A get function for the width of the rectangle"""
        return self.__height


    @height.setter
    def height(self, value):
        """Set method for the height property"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
