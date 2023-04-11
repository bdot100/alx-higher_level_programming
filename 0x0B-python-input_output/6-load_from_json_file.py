#!/usr/bin/python3
"""This function creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file."""
    with open(filename) as myfile:
        return json.load(myfile)
