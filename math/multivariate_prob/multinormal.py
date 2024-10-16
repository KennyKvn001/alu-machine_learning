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
                              - d is the number of dimensions for
                              each data point
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
        # Set the number of dimensions
        self.d = d

        # Compute the mean vector of shape (d, 1)
        self.mean = np.mean(data, axis=1, keepdims=True)

        # Center the data by subtracting the mean (shape (d, n))
        data_centered = data - self.mean

        # Compute the covariance matrix of shape (d, d)
        self.cov = np.dot(data_centered, data_centered.T) / (n - 1)

        self.cov_inv = np.linalg.inv(self.cov)
        self.cov_det = np.linalg.det(self.cov)

    def pdf(self, x):
        """
        Calculates the PDF at a given data point x.

        Parameters:
        x (numpy.ndarray): A numpy array of shape (d, 1), where d is
        the number of dimensions for the data point.

        Returns:
        float: The value of the PDF at the given data point.

        Raises:
        TypeError: If x is not a numpy.ndarray.
        ValueError: If x does not have the shape (d, 1).
        """

        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        if x.shape != (self.d, 1):
            raise ValueError(f"x must have the shape ({self.d}, 1)")

        # Calculate the PDF using the multivariate Gaussian formula
        diff = x - self.mean  # Difference between x and the mean
        exponent = -0.5 * np.dot(np.dot(diff.T, self.cov_inv), diff)  # Exponent term
        denominator = np.sqrt((2 * np.pi) ** self.d * self.cov_det)  # Denominator term

        pdf_value = (1 / denominator) * np.exp(exponent)  # PDF value

        return pdf_value[0, 0]  # Return as a scalar value
