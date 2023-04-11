#!/usr/bin/python3
"""This Module inserts a line of text to a file."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing a specific string 

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as myfile:
        for line in myfile:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as write_file:
        write_file.write(text)

