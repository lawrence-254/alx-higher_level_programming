#!/usr/bin/python3
"""Defines a class base model."""
import json
import csv
import turtle


class Base:
    """Base model class.

    Private Attribute:
        __nb_object(int): number of bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Defines a new base.

        Args:
            id (int): an integer identifier for the new base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
