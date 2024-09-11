#!/usr/bin/env python3
"""
Module `7-getting_cozy`
This module contains a function that concatenate two
matrices along a specific axis
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two 2D matrices along a specific axis.

    Args:
        mat1 (list of lists of int/float): The first matrix.
        mat2 (list of lists of int/float): The second matrix.
        axis (int): The axis along which to concatenate
        (0 for rows, 1 for columns).

    Returns:
        list of lists of int/float: A new matrix with
        concatenated elements.
        None: If the matrices cannot be concatenated
        due to incompatible dimensions.
    """

    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None

        return mat1 + mat2

    elif axis == 1:
        if len(mat1) != len(mat2):
            return None

        result = [row1 + row2 for row1, row2 in zip(mat1, mat2)]
        return result

    return None
