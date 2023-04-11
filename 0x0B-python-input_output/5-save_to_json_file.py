#!/usr/bin/python3
"""This function writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Function Writes an object to a text file using JSON representation."""
    with open(filename, "w") as myfile:
        json.dump(my_obj, myfile)

