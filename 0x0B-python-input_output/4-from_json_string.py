#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a string from JSON function."""
import json


def from_json_string(my_str):
    """Returns a Python data structure represented by a JSON string."""
    return json.loads(my_str)
