#!/usr/bin/python3
"""Defines a function that appends a file."""


def append_write(filename="", text=""):
    """Appends at the end of a UTF8 text file.

    Args:
        filename (str)
        text (str)
    Returns:
        Size of appended characters.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
