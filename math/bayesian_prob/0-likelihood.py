#!/usr/bin/env python3
"""Module that calculates the likelihood of obtainong the data
given various probabilities"""

import numpy as np
from scipy.stats import binom


def likelihood(x, n, P):
    """
     Calculate the likelihood of obtaining observed data for various hypothetical probabilities
    of developing severe side effects in a drug trial.

    This function uses the binomial distribution to model the probability of observing
    a certain number of patients with severe side effects given different probabilities
    of side effect occurrence.

    Parameters:
    -----------
    x : int
        The number of patients that develop severe side effects.
    n : int
        The total number of patients observed in the trial.
    P : numpy.ndarray
        A 1D array containing various hypothetical probabilities of developing severe side effects.

    Returns:
    --------
    numpy.ndarray
        A 1D array containing the likelihood of obtaining the observed data (x out of n)
        for each probability in P, respectively.
    """
    # Input validation
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    if not isinstance(x, int) or x < 0:
        raise ValueError("x must be an integer that is greater than or equal to 0")

    if x > n:
        raise ValueError("x cannot be greater than n")

    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")

    if np.any((P < 0) | (P > 1)):
        raise ValueError("All values in P must be in the range [0, 1]")

    # Calculate likelihood using binomial distribution
    return binom.pmf(x, n, P)
