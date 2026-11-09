#!/usr/bin/python3
"""Defines a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Writes text to a text file (UTF8) and returns the characters written.

    The file is created if it does not exist and overwritten if it does.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
