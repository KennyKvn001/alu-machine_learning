#!/usr/bin/env python3
"""
This script contains a function to calculate the integral
of a polynomial.
"""


def poly_integral(poly, C=0):
    """
    This function computes the integral of a polynomial
    represented by a list of coefficients.

    Parameters:
    - poly: A list of coefficients, where the index of each
    element represents the power of x.
    - C: An optional integer representing the constant
    of integration (default is 0).

    Returns:
    - A new list of coefficients representing the
    integral of the polynomial.
      If the result contains a term with a whole number,
      it should be returned as an integer.
      If the input poly or C are not valid,
      the function returns None.
    """

    if not isinstance(poly, list) or not isinstance(C, (int, float)):
        return None
    if not all(isinstance(coef, (int, float)) for coef in poly):
        return None

    integral = [C]
    # Iterate through the coefficients of the input polynomial.
    for i, coef in enumerate(poly):
        # Calculate the new coefficient after integrating (coef / (i + 1))
        new_coef = coef / (i + 1)

        # If the result is a whole number, convert it to an integer.
        if new_coef.is_integer():
            new_coef = int(new_coef)

        integral.append(new_coef)

    # Add the constant of integration C as the constant term (for x^0)
    integral.insert(0, C)

    return integral
