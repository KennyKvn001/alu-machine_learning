#!/usr/bin/env python3
"""Module that calculate the correlation matrix from a given
covariance matrix"""

import numpy as np


def correlation(C):
    """
    Calculates the correlation matrix from a given covariance matrix.

    Parameters:
    C (numpy.ndarray): A covariance matrix of shape (d, d).
                       - d is the number of dimensions.

    Returns:
    numpy.ndarray: A correlation matrix of shape (d, d).

    Raises:
    TypeError: If C is not a numpy.ndarray.
    ValueError: If C is not a 2D square matrix.
    """

    # Validate the input type
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")

    # Validate the input shape (C must be a 2D square matrix)
    if C.ndim != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    # Get the standard deviations from the covariance matrix
    std_devs = np.sqrt(np.diag(C))

    # Prevent division by zero in case of zero variance
    if np.any(std_devs == 0):
        raise ValueError("Covariance matrix contains zero variance")

    # Create the correlation matrix by dividing covariance by the outer
    # product of standard deviations
    corr_matrix = C / np.outer(std_devs, std_devs)

    return corr_matrix
