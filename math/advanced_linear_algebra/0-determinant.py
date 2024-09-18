#!/usr/bin/env python3
"""
Module `0-determinat`
This module Calculates the determinant of a square matrix
"""


def determinant(matrix):
    """
    Calculate the determinant of a square matrix.

    Args:
    matrix (list of lists):
    The input matrix whose determinant is to be calculated.
    Each inner list represents a row of the matrix.

    Returns:
    float or int: The determinant of the input matrix.

    Raises:
    TypeError: If the input is not a list of lists.
    ValueError: If the input matrix is not square (i.e.,
    number of rows != number of columns).

    """

    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if n == 1 and len(matrix[0]) == 0:
        return 1

    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a square matrix")

    if n == 0:
        return 1
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for j in range(n):
        submatrix = [row[:j] + row[j + 1:] for row in matrix[1:]]
        sign = (-1) ** j
        det += sign * matrix[0][j] * determinant(submatrix)

    return det
