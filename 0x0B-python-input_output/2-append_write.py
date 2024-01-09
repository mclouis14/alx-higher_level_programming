#!/usr/bin/python3
"""Defines a text-file appending function."""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF-8)
    Args:
        filename (str): Name of the file to be appended.
        text (str): The string to be appended to the file.
    Returns:
        Number of characters appended to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
