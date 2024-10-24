#!/usr/bin/env python3
"""Module grayscale"""
import numpy as np


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
    # Extract dimensions of the images and kernel
    m, h, w = images.shape
    kh, kw = kernel.shape

    # Calculate the output dimensions after valid convolution
    nh = h - kh + 1
    nw = w - kw + 1

    # Initialize the output array for the convolved images
    convolved = np.zeros((m, nh, nw))

    # Perform the convolution
    for i in range(nh):
        for j in range(nw):
            # Extract the patch from each image that corresponds to the kernel
            # size
            image_patch = images[:, i: i + kh, j: j + kw]
            # Perform element-wise multiplication and sum the results over axis
            # 1 and 2 (height and width)
            convolved[:, i, j] = np.sum(
                np.multiply(image_patch, kernel), axis=(1, 2))

    return convolved
