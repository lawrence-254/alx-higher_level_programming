#!/usr/bin/python3
"""Defines a function that turns python class to JSON."""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
