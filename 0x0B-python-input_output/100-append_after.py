#!/usr/bin/python3
"""Defines a function used to insert text into a file."""


def append_after(filename="", search_string="", new_string=""):
    """Appends text to a file.

    Args:
        filename (str)
        search_string (str)
        new_string (str)
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
