#!/usr/bin/env python3
"""Module grayscale"""
import numpy as np


def convolve_grayscale_valid(images, kernel):
    """
    Performs a valid convolution on grayscale images.

    Args:
        images (numpy.ndarray): A numpy array of shape (m, h, w)
        containing multiple grayscale images,
                                where:
                                - m is the number of images.
                                - h is the height in pixels of the images.
                                - w is the width in pixels of the images.
        kernel (numpy.ndarray): A numpy array of shape (kh, kw)
        containing the kernel for the convolution,
                                where:
                                - kh is the height of the kernel.
                                - kw is the width of the kernel.

    Returns:
        numpy.ndarray: A numpy array containing the convolved
        images with reduced dimensions (valid convolution).
    """
    m, h, w = images.shape[0], images.shape[1], images.shape[2]
    kh, kw = kernel.shape[0], kernel.shape[1]
    nw = w - kw + 1
    nh = h - kh + 1
    convolved = np.zeros((m, nh, nw))
    for i in range(nh):
        for j in range(nw):
            image = images[:, i: (i + kh), j: (j + kw)]
            convolved[:, i, j] = np.sum(
                np.multiply(image, kernel), axis=(1, 2))
    return convolved
