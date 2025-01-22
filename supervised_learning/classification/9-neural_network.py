#!/usr/bin/env python3
"""Module that defines a neural network with one hidden layer
 performing binary classification."""
import numpy as np


class NeuralNetwork:
    """A neural network with one hidden layer performing
    binary classification."""

    def __init__(self, nx, nodes):
        """
        Initializes the neural network.

        Args:
            nx (int): The number of input features.
            nodes (int): The number of nodes in the hidden layer.

        Raises:
            TypeError: If nx is not an integer or nodes is not an integer.
            ValueError: If nx is less than 1 or nodes is less than 1.
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        # Initialize weights and biases for the hidden layer
        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0  # Activated output for the hidden layer

        # Initialize weights and biases for the output layer
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0
        self.__A2 = 0  # Activated output for the output neuron

    @property
    def W1(self):
        """Getter for W1."""
        return self.__W1

    @property
    def b1(self):
        """Getter for b1."""
        return self.__b1

    @property
    def A1(self):
        """Getter for A1."""
        return self.__A1

    @property
    def W2(self):
        """Getter for W2."""
        return self.__W2

    @property
    def b2(self):
        """Getter for b2."""
        return self.__b2

    @property
    def A2(self):
        """Getter for A2."""
        return self.__A2

    def forward_prop(self, X):
        """
        Calculates the forward propagation of the neural network.

        Args:
            X (numpy.ndarray): Input data of shape (nx, m).

        Returns:
            tuple: Activated outputs A1 and A2.
        """
        Z1 = np.matmul(self.__W1, X) + self.__b1
        self.__A1 = 1 / (1 + np.exp(-Z1))  # Sigmoid activation

        Z2 = np.matmul(self.__W2, self.__A1) + self.__b2
        self.__A2 = 1 / (1 + np.exp(-Z2))  # Sigmoid activation

        return self.__A1, self.__A2
