#!/usr/bin/env python3

"""
Module `8-riding_bareback`
This module contains a function that perform matrices
multiplication using the bareback method.
"""


def mat_mul(mat1, mat2):
    """
    Multiplies two 2D matrices (mat1 and mat2).

    Args:
        mat1 (list of lists of int/float): The first matrix.
        mat2 (list of lists of int/float): The second matrix.

    Returns:
        list of lists of int/float: The resulting matrix from
        multiplying mat1 and mat2.
        None: If the matrices cannot be multiplied due to
        incompatible dimensions.
    """
    m, n = len(mat1), len(mat1[0])
    p, q = len(mat2), len(mat2[0])

    if n != p:
        return None

    result = [[0 for _ in range(q)] for _ in range(m)]

    for i in range(m):
        for j in range(q):
            for k in range(n):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result
