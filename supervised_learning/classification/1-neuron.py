#!/usr/bin/env python3
"""Module that defines a single neuron performing binary classification"""
import numpy as np


class Neuron:
    """A single neuron performing binary classification."""

    def __init__(self, nx):
        """
        Initializes the neuron.

        Args:
            nx (int): The number of input features to the neuron.

        Raises:
            TypeError: If nx is not an integer.
            ValueError: If nx is less than 1.
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be positive")

        # Initialize private attributes
        self.__W = np.random.randn(1, nx)
        self.__b = 0  # Bias (initialized to 0)
        self.__A = 0  # Activated output (initialized to 0)

    @property
    def W(self):
        """Getter for the weights vector."""
        return self.__W

    @property
    def b(self):
        """Getter for the bias."""
        return self.__b

    @property
    def A(self):
        """Getter for the activated output."""
        return self.__A

    @A.setter
    def A(self, value):
        """Setter for the activated output."""
        self.__A = value

    def forward_prop(self, X):
        """
        Performs forward propagation for the neuron.

        Args:
            X (numpy.ndarray): Input data of shape (nx, m), where m is the number of examples.

        Returns:
            numpy.ndarray: The activated output of the neuron.
        """
        # Ensure X has the correct shape (nx, m)
        if X.shape[0] != self.__W.shape[1]:
            raise ValueError(f"Input X must have shape ({self.__W.shape[1]}, m)")

        # Linear transformation: Z = W.X + b
        Z = np.dot(self.__W, X) + self.__b

        # Sigmoid activation: A = 1 / (1 + exp(-Z))
        self.__A = 1 / (1 + np.exp(-Z))

        return self.__A
