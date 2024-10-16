#!/usr/bin/env python3
import numpy as np

""" Mean Cov is module that Calculates the mean and
covariance of a dataset."""


def mean_cov(X):
    """
    Calculates the mean and covariance of a dataset.

    Parameters:
    X (numpy.ndarray): A numpy array of shape (n, d) containing the dataset.
                       - n is the number of data points.
                       - d is the number of dimensions in each data point.

    Returns:
    tuple: A tuple (mean, cov):
           - mean is a numpy.ndarray of shape (1, d) containing
           the mean of the dataset.
           - cov is a numpy.ndarray of shape (d, d) containing the
           covariance matrix of the dataset.

    Raises:
    TypeError: If X is not a 2D numpy.ndarray.
    ValueError: If X contains less than 2 data points.
    """

    # Validate input type and dimensions
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        raise TypeError("X must be a 2D numpy.ndarray")

    n, d = X.shape

    # Validate that there are at least 2 data points
    if n < 2:
        raise ValueError("X must contain multiple data points")

    # Calculate the mean (1, d)
    mean = np.mean(X, axis=0).reshape(1, d)

    # Center the data by subtracting the mean
    X_centered = X - mean

    # Calculate the covariance matrix (d, d)
    cov = np.dot(X_centered.T, X_centered) / (n - 1)

    return mean, cov
