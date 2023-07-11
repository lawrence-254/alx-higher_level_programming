#!/usr/bin/python3
"""Defines a function for writting JSON."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to text using JSON."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
