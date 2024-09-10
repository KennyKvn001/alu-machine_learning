#!/usr/bin/env python3

"""
Module `4-line_up`
This module contains a function that adds two arrays
element-wise
"""


def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise.

    Args:
        arr1 (list of int/float): The first array.
        arr2 (list of int/float): The second array.

    Returns:
        list of int/float: A new list with element-wise sums.
        None: If the arrays are not of the same shape.
    """

    if len(arr1) != len(arr2):
        return None
    result = []

    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[i])

    return result
