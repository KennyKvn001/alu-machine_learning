#!/usr/bin/env python3
"""
Module `3-adjugate`
This module calculates the adjugate matrix of a given square matrix
"""


def adjugate(matrix):
    """
    Calculate the adjugate matrix of a given square matrix.

    The adjugate matrix is the transpose of the cofactor matrix.

    Args:
    matrix (list of lists): The input matrix whose adjugate matrix
    is to be calculated.
    Each inner list represents a row of the matrix.

    Returns:
    list of lists: The adjugate matrix of the input matrix.

    Raises:
    TypeError: If the input is not a list of lists.
    ValueError: If the input matrix is not square or is empty.
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

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

    cofactor_matrix = []
    for i in range(n):
        cofactor_row = []
        for j in range(n):
            minor_det = determinant(minor(matrix, i, j))
            cofactor_row.append((-1) ** (i + j) * minor_det)
        cofactor_matrix.append(cofactor_row)

    adjugate_matrix = [[cofactor_matrix[j][i]
                        for j in range(n)] for i in range(n)]

    return adjugate_matrix
