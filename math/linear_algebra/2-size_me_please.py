#!/usr/bin/env python3


def matrix_shape(matrix):
    """
    Returns the shape of a matrix (a list of lists) as a list of integers.

    The shape of a matrix is a list of integers, where each integer represents
    the number of elements in each dimension of the matrix. For example, a 2x3
    matrix would have a shape of [2, 3].

    Args:
        matrix (list): A list of lists, representing a matrix.

    Returns:
        list: A list of integers, representing the shape of the matrix.

    Example:
        >>> matrix_shape([[1, 2, 3], [4, 5, 6]])
        [2, 3]
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
