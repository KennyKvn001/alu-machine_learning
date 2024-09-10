#!/usr/bin/env python3
"""
Module `2-size_me_please`

This module provides a function to calculate the shape of a matrix.

Functions:
    - matrix_shape(matrix): Returns the shape of a given matrix as a
    list of integers.
"""


def matrix_shape(matrix):
    """
    Calculates the shape of a given matrix.

    Args:
        matrix (list): A list of lists representing the matrix.

    Returns:
        list: A list of integers representing the dimensions of the matrix.
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
