#!/usr/bin/env python3
"""Module grayscale"""

import numpy as np


def convolve_grayscale_same(images, kernel):
    """
    Performs a same convolution on grayscale images.

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
        numpy.ndarray: A numpy array of shape (m, h, w) containing the convolved images.
    """
    # Extract dimensions of images and kernel
    m, h, w = images.shape
    kh, kw = kernel.shape

    # Determine the padding needed for height and width (same convolution)
    pad_h = (kh - 1) // 2
    pad_w = (kw - 1) // 2

    # Pad images with zeros
    padded_images = np.pad(
        images, ((0, 0), (pad_h, pad_h), (pad_w, pad_w)), mode="constant"
    )

    # Initialize the output array for the convolved images
    output = np.zeros((m, h, w))

    # Iterate over each image
    for i in range(m):
        # Iterate over the height and width of the image
        for y in range(h):
            for x in range(w):
                # Perform element-wise multiplication and summing for convolution
                output[i, y, x] = np.sum(
                    kernel * padded_images[i, y : y + kh, x : x + kw]
                )

    return output
