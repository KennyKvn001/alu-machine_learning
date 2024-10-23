#!/usr/bin/env python3
"""Module grayscale"""
import numpy as np


def convolve_grayscale_valid(images, kernel):
    """
    Performs a valid convolution on grayscale images.

    Args:
        images (numpy.ndarray):
        A numpy array of shape (m, h, w) containing multiple grayscale images,
                                where:
                                - m is the number of images.
                                - h is the height in pixels of the images.
                                - w is the width in pixels of the images.
        kernel (numpy.ndarray):
        A numpy array of shape (kh, kw) containing the kernel for the convolution,
                                where:
                                - kh is the height of the kernel.
                                - kw is the width of the kernel.

    Returns:
        numpy.ndarray: A numpy array containing the convolved
        images with reduced dimensions.
    """
    # Extract dimensions of images and kernel
    m, h, w = images.shape
    kh, kw = kernel.shape

    # Calculate the output dimensions after valid convolution
    output_h = h - kh + 1
    output_w = w - kw + 1

    # Initialize the output array for the convolved images
    output = np.zeros((m, output_h, output_w))

    # Iterate over each image
    for i in range(m):
        # Iterate over the height and width of the valid output space
        for y in range(output_h):
            for x in range(output_w):
                # Perform element-wise multiplication and summing for convolution
                output[i, y, x] = np.sum(kernel * images[i, y : y + kh, x : x + kw])

    return output
