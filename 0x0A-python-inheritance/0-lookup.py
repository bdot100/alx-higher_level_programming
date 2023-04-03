#!/usr/bin/python3
"""Defines an object attribute lookup function that lists available attributes and methods of an object"""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
