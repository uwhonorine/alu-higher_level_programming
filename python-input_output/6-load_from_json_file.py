#!/usr/bin/python3
"""Defines a function that creates an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Returns the object represented by the JSON text file filename."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
