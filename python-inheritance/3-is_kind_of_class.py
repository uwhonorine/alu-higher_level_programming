#!/usr/bin/python3
"""Defines a function that checks if an object is of a kind of class."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or of a subclass of it.

    Otherwise returns False.
    """
    return isinstance(obj, a_class)
