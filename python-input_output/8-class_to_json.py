#!/usr/bin/python3
"""Defines a function that describes an object as a simple dictionary."""


def class_to_json(obj):
    """Returns the dictionary description of obj for JSON serialization.

    All the attributes of obj must be serializable: list, dictionary,
    string, integer or boolean.
    """
    return obj.__dict__.copy()
