#!/usr/bin/python3
"""This function reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """This function reads a text file (UTF8) and prints it to stdout."""
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end="")
