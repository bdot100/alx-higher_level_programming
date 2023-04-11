#!/usr/bin/python3
"""This Module appends a string at the end of a text file (UTF8) and returns the number of characters added"""


def append_write(filename="", text=""):
    """This Module appends a string at the end of a text file (UTF8) and returns the number of characters added
    Args:
        filename (str): The name of the file you want to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as myfile:
        return myfile.write(text)

