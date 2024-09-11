#!/usr/bin/env python3

"""
Module `6-howdy_partner`
This module contains a function that concatenates two arrays
"""


def cat_arrays(arr1, arr2):
    """
    Concatenates two arrays.

    Args:
        arr1 (list of int/float): The first array.
        arr2 (list of int/float): The second array.

    Returns:
        list of int/float: A new list containing all elements
        of arr1 followed by all elements of arr2.
    """
    result = arr1 + arr2
    return result
