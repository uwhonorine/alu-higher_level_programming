#!/usr/bin/python3
"""Defines a function that checks if an object inherited from a class."""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a subclass of a_class.

    The class of obj must inherit (directly or indirectly) from a_class
    without being a_class itself. Otherwise returns False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
