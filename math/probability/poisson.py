#!/usr/bin/env python3
"""
Poisson distribution
"""


class Poisson:
    """Poisson distribution class."""

    def __init__(self, data=None, lambtha=1.0):
        """
        Initialize the Poisson distribution.

        :param data: List of data points to estimate the
        distribution (default is None)
        :param lambtha: The expected number of occurrences
        in a given time frame (default is 1)
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

    def pmf(self, k):
        """
        Calculate the PMF for a given number of 'successes'.

        :param k: Number of successes
        :return: PMF value for the given k
        """
        if k < 0:
            return 0

        # Convert k to an integer if it's not already
        k = int(k)

        # Calculate the PMF using the Poisson formula: (e^(-λ) * λ^k) / k!
        lambtha = self.lambtha
        e_term = math.exp(-lambtha)
        lambda_term = lambtha**k
        factorial_k = math.factorial(k)

        pmf_value = (e_term * lambda_term) / factorial_k
        return pmf_value
