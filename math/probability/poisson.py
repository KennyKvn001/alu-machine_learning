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

    def factorial(self, n):
        """Manually calculates the factorial of a number n."""
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def exp(self, x):
        """Manually calculates the exponential of x
        using a Taylor series expansion."""
        result = 1  # The sum of the series starts with 1 (i.e., x^0 / 0!)
        term = 1  # Term is the individual terms of the series
        for i in range(1, 100):  # We use 100 terms for approximation
            term *= x / i
            result += term
        return result

    def pmf(self, k):
        """
        calculates the value of the PMF for a given number of successes

        parameters:
            k [int]: number of successes
                If k is not an int, convert it to int
                If k is out of range, return 0

        return:
            the PMF value for k
        """
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        e = 2.7182818285
        lambtha = self.lambtha
        factorial = 1
        for i in range(k):
            factorial *= i + 1
        pmf = ((lambtha**k) * (e**-lambtha)) / factorial
        return pmf

    def cdf(self, k):
        """
        calculates the value of the CDF for a given number of successes

        parameters:
            k [int]: number of successes
                If k is not an int, convert it to int
                If k is out of range, return 0

        return:
            the CDF value for k
        """
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        cdf = 0
        for i in range(k + 1):
            cdf += self.pmf(i)
        return cdf
