#!/usr/bin/python3
"""Defines a function that reads a JSON file."""
import json


def load_from_json_file(filename):
    """Create a python object using JSON file."""
    with open(filename) as f:
        return json.load(f)
