"""
Module `3-flip_me_over`
This is the function that transpose a matrix
"""


def matrix_transpose(matrix):
    """
    Returns the transpose of a 2D matrix.

    Args:
        matrix (list of lists): The input 2D matrix.

    Returns:
        list of lists: The transposed matrix.
    """
    # Use zip to transpose the matrix and convert the result back to a list of lists
    return [list(row) for row in zip(*matrix)]
