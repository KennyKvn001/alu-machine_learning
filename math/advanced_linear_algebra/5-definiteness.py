#!/usr/bin/env python3
"""
Module `5-definiteness`
This module calculates the definiteness of a given matrix
"""


import numpy as np


def definiteness(matrix):
    """
    Calculate the definiteness of a given square matrix.

    Args:
    matrix (numpy.ndarray): The input matrix whose definiteness
    is to be calculated.
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
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        return None

    if not np.allclose(matrix, matrix.T):
        return None

    try:
        eigenvalues = np.linalg.eigvals(matrix)
    except np.linalg.LinAlgError:
        return None

    pos_eig = np.sum(eigenvalues > 1e-10)
    neg_eig = np.sum(eigenvalues < -1e-10)
    zero_eig = np.sum(np.isclose(eigenvalues, 0, atol=1e-10))

    if pos_eig == len(eigenvalues):
        return "Positive definite"
    elif pos_eig + zero_eig == len(eigenvalues) and pos_eig > 0:
        return "Positive semi-definite"
    elif neg_eig == len(eigenvalues):
        return "Negative definite"
    elif neg_eig + zero_eig == len(eigenvalues) and neg_eig > 0:
        return "Negative semi-definite"
    elif pos_eig > 0 and neg_eig > 0:
        return "Indefinite"
    else:
        return None
