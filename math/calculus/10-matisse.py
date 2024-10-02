#!/usr/bin/env python3
"""
This script contains a function to calculate the derivative
of a polynomial.
"""


def poly_derivative(poly):
    """
    This function calculates the derivative of a polynomial.

    Parameters:
    poly (list): The coefficients of the polynomial in
    descending order of power.

    Returns:
    list: The coefficients of the derivative of the polynomial.
    Returns None if poly is not a list, is empty, or contains
    non-numeric elements.
    """

    if (
        not isinstance(poly, list)
        or len(poly) == 0
        or not all(isinstance(c, (int, float)) for c in poly)
    ):
        return None
    # Compute the derivative
    derivative = [poly[i] * i for i in range(1, len(poly))]

    # If derivative is all zeros, return [0]
    if all(c == 0 for c in derivative):
        return [0]

    return derivative
