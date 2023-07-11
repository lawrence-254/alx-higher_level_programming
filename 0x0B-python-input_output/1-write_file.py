#!/usr/bin/python3
"""Defines a function that writes a file."""


def write_file(filename="", text=""):
    """Writes to a UTF8 text file.

    Args:
        filename (str)
        text (str)
    Returns:
        Size of the file in character count.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
