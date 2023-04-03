#!/usr/bin/python3
"""This is a module that inherits from the list class"""


class MyList(list):
    """This class inherits from list class"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
