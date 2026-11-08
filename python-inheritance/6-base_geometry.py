#!/usr/bin/python3
"""Defines a class BaseGeometry with an area method to implement."""


class BaseGeometry:
    """A base class for geometry classes."""

    def area(self):
        """Raises an Exception: area() must be implemented by subclasses."""
        raise Exception("area() is not implemented")
