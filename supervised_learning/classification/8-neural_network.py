#!/usr/bin/env python3
"""Module that defines a neural network with one hidden layer performing binary classification."""
import numpy as np


class NeuralNetwork:
    """A neural network with one hidden layer performing binary classification."""

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
        self.W1 = np.random.randn(nodes, nx)
        self.b1 = np.zeros((nodes, 1))
        self.A1 = 0  # Activated output for the hidden layer

        # Initialize weights and biases for the output layer
        self.W2 = np.random.randn(1, nodes)
        self.b2 = 0
        self.A2 = 0  # Activated output for the output neuron
