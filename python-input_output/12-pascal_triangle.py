#!/usr/bin/python3
"""Defines a function that builds Pascal's triangle."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle.

    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for _ in range(1, n):
        previous = triangle[-1]
        row = [1]
        for i in range(len(previous) - 1):
            row.append(previous[i] + previous[i + 1])
        row.append(1)
        triangle.append(row)
    return triangle
