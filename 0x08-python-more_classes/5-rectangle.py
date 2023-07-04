#!/usr/bin/python3
"""Defines a Rectangle with dimensions."""


class Rectangle:
    """A rectangle class."""

    def __init__(self, width=0, height=0):
        """Rectangle initialisation with dimension defined

        Args:
            width(int):width is the shortest side
            height(int):the the longer side
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """A get function for the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """A set function for the width property that ensures it is an int."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """A get function for the width of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set method for the height property."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area occupied by the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns th total distance around the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """print the rectangle with the character #."""

        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        return False
