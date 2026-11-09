#!/usr/bin/python3
"""Defines a class Student with a filtered dictionary representation."""


class Student:
    """A student defined by a first name, a last name and an age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a student.

        Args:
            first_name: the first name of the student.
            last_name: the last name of the student.
            age: the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation of the student.

        If attrs is a list of strings, only the attributes whose names are
        in this list are retrieved. Otherwise, all the attributes are.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {a: self.__dict__[a] for a in attrs if a in self.__dict__}
        return self.__dict__.copy()
