#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF-8)
    Args:
        filename (str): Name of the text file to be written.
        text (str): The string to be written to the file.
    Returns:
        Number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
