#!/usr/bin/env python3
"""
Module Calculate the posterior probability for various
hypothetical probabilities of
developing severe side effects given the observed data
in a drug trial.
"""

import numpy as np
from scipy.stats import binom


def posterior(x, n, P, Pr):
    """
    Calculate the posterior probability for various
    hypothetical probabilities of
    developing severe side effects given the observed
    data in a drug trial.

    This function uses Bayes' theorem to compute the
    posterior probability,
    combining the likelihood (based on the binomial distribution)
    with the prior beliefs.

    Parameters:
    -----------
    x : int
        The number of patients that develop severe side effects.
    n : int
        The total number of patients observed in the trial.
    P : numpy.ndarray
        A 1D array containing various hypothetical probabilities of
        developing severe side effects.
    Pr : numpy.ndarray
        A 1D array containing the prior beliefs of P.

    Returns:
    --------
    numpy.ndarray
        The posterior probability of each probability in P given x and n.

    Raises:
    -------
    ValueError
        If n is not a positive integer.
        If x is not a non-negative integer.
        If x is greater than n.
        If any value in P or Pr is not in the range [0, 1].
        If Pr does not sum to 1.
    TypeError
        If P is not a 1D numpy.ndarray.
        If Pr is not a numpy.ndarray with the same shape as P.
    """
    # Input validation
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0")

    if x > n:
        raise ValueError("x cannot be greater than n")

    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")

    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")

    if np.any((P < 0) | (P > 1)):
        raise ValueError("All values in P must be in the range [0, 1]")

    if np.any((Pr < 0) | (Pr > 1)):
        raise ValueError("All values in Pr must be in the range [0, 1]")

    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")

    # Calculate likelihood using binomial distribution
    likelihood = binom.pmf(x, n, P)

    # Calculate marginal probability
    marginal = np.sum(likelihood * Pr)

    # Calculate posterior probability
    posterior = (likelihood * Pr) / marginal

    return posterior
