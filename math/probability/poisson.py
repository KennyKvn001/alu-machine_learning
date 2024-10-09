#!/usr/bin/env python3
"""
Poisson distribution
"""


class Poisson:
    """Poisson distribution class."""

    def __init__(self, data=None, lambtha=1.0):
        """
        Initialize the Poisson distribution.

        :param data: List of data points to estimate the distribution (default is None)
        :param lambtha: The expected number of occurrences in a given time frame (default is 1)
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            # Calculate lambtha as the average of the data points
            self.lambtha = float(sum(data) / len(data))
