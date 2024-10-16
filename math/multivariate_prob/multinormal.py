#!/usr/bin/env python3
"""Multinomal CLass"""
import numpy as np


class MultiNormal:
    """
    Represents a Multivariate Normal distribution.
    """

    def __init__(self, data):
        """
        Initializes the MultiNormal class.

        Parameters:
        data (numpy.ndarray): A 2D numpy array of shape (d, n), where:
                              - d is the number of dimensions for each data point
                              - n is the number of data points

        Raises:
        TypeError: If data is not a 2D numpy.ndarray.
        ValueError: If the number of data points n is less than 2.
        """

        # Validate input type and dimensions
        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape

        # Ensure that there are at least 2 data points
        if n < 2:
            raise ValueError("data must contain multiple data points")

        # Compute the mean vector of shape (d, 1)
        self.mean = np.mean(data, axis=1, keepdims=True)

        # Center the data by subtracting the mean (shape (d, n))
        data_centered = data - self.mean

        # Compute the covariance matrix of shape (d, d)
        self.cov = np.dot(data_centered, data_centered.T) / (n - 1)
