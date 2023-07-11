#!/usr/bin/python3
"""Defines a function that turns string to JSON"""
import json


def to_json_string(my_obj):
    """Returns JSON"""
    return json.dumps(my_obj)
