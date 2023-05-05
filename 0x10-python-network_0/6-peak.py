#!/usr/bin/python3
"""This script find the peak from an unsorted integer """


def find_peak(list_of_integers):
    """
    Args: list_of_integers(int): list of integers to find the peak from
    Returns: Peak from the list or None
    """

    left, right = 0, len(list_of_integers) - 1
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return list_of_integers[left]
