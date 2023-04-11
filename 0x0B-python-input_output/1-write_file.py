#!/usr/bin/python3
"""This function writes a string to a text file (UTF8) and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """This function writes a string to a text file (UTF8) and returns the number of characters written

    Args:
        filename (str): The name of the file to write.
        text (str): The text you want to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        return my_file.write(text)

