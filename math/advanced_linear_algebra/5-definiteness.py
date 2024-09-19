#!/usr/bin/env python3
"""
Module `5-definiteness`
This module calculates the definiteness of a given matrix
"""


def definiteness(matrix):
    """
    Calculate the definiteness of a given square matrix.

    Args:
    matrix (numpy.ndarray): The input matrix whose definiteness is to be calculated.
                            It should be a square matrix of shape (n, n).

    Returns:
    str or None: The definiteness of the matrix as a string,
    or None if the matrix is not valid.
    Possible return values are:
        - "Positive definite"
        - "Positive semi-definite"
        - "Negative semi-definite"
        - "Negative definite"
        - "Indefinite"
        - None (if the matrix doesn't fit any category or is not valid)

    Raises:
    TypeError: If the input is not a numpy.ndarray.
    """

    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        return None

    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        return None

    for i in range(n):
        for j in range(i + 1, n):
            if abs(matrix[i][j] - matrix[j][i]) > 1e-10:
                return None

    def determinant(mat):
        """Calculate the determinant of a matrix."""
        size = len(mat)
        if size == 1:
            return mat[0][0]
        if size == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        det = 0
        for j in range(size):
            submatrix = [row[:j] + row[j + 1:] for row in mat[1:]]
            det += ((-1) ** j) * mat[0][j] * determinant(submatrix)
        return det

    determinants = []
    for i in range(1, n + 1):
        submatrix = [row[:i] for row in matrix[:i]]
        determinants.append(determinant(submatrix))

    pos_def = all(d > 1e-10 for d in determinants)
    pos_semi_def = all(d >= -1e-10 for d in determinants) and any(
        d > 1e-10 for d in determinants
    )
    neg_def = all((-1) ** (i + 1) * d > 1e-10 for i,
                  d in enumerate(determinants))
    neg_semi_def = all(
        (-1) ** (i + 1) * d >= -1e-10 for i, d in enumerate(determinants)
    ) and any((-1) ** (i + 1) * d > 1e-10 for i, d in enumerate(determinants))

    if pos_def:
        return "Positive definite"
    elif pos_semi_def:
        return "Positive semi-definite"
    elif neg_def:
        return "Negative definite"
    elif neg_semi_def:
        return "Negative semi-definite"
    elif any(d > 1e-10 for d in determinants) and any(d < -1e-10 for d in determinants):
        return "Indefinite"
    else:
        return None
