#!/usr/bin/env python3
"""
Module `2-cofactor`
This module calculate the  cofactor matrix of a given sqaure matrix
"""


def cofactor(matrix):
    """
    Calculate the cofactor matrix of a given square matrix.

    The cofactor matrix is derived from the minor matrix by checkerboard
    negation (alternating signs).

    Args:
    matrix (list of lists): The input matrix whose cofactor matrix
    is to be calculated.
    Each inner list represents a row of the matrix.

    Returns:
    list of lists: The cofactor matrix of the input matrix.

    Raises:
    TypeError: If the input is not a list of lists.
    ValueError: If the input matrix is not square or is empty.
    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Check if matrix is non-empty and square
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    # Special case for 1x1 matrix
    if n == 1:
        return [[1]]

    def minor(mat, i, j):
        """Calculate the minor of matrix mat for element at (i, j)."""
        return [row[:j] + row[j + 1:] for row in (mat[:i] + mat[i + 1:])]

    def determinant(mat):
        """Calculate the determinant of a matrix."""
        if len(mat) == 1:
            return mat[0][0]
        if len(mat) == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        det = 0
        for j in range(len(mat)):
            det += ((-1) ** j) * mat[0][j] * determinant(minor(mat, 0, j))
        return det

    # Calculate cofactor matrix
    cofactor_matrix = []
    for i in range(n):
        cofactor_row = []
        for j in range(n):
            minor_det = determinant(minor(matrix, i, j))
            cofactor_row.append((-1) ** (i + j) * minor_det)
        cofactor_matrix.append(cofactor_row)

    return cofactor_matrix
