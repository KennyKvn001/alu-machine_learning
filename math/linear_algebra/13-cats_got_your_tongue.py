#!/usr/bin/env python3
"""
Module `13-cats_got_your_tongue`
This module contains a function that
that concatenates two matrices along a specific axis
"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    this function that
    that concatenates two matrices along a specific axis
    """
    return np.concatenate((mat1, mat2), axis=axis)
