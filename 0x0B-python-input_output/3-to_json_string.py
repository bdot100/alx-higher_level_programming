#!/usr/bin/python3
"""This function returns the JSON representation of an object (string)."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of a string object."""
    return json.dumps(my_obj)
