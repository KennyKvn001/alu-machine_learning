#!/usr/bin/env python3


def matrix_shape(matrix):
    """
    This function takes a matrix as input and returns its shape.
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
