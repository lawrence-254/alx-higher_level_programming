#!/usr/bin/python3
"""Defines a class based on 6-base_geometry.py."""


class BaseGeometry:
    """Defines propeties of the class."""

    def area(self):
        """Raises exception while not implementing area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if values are integer.

        Args:
            name (str).
            value (int).

        Raises:
            ValueError: if value is less or equal 0.
            TypeError: not an int.
        """
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
