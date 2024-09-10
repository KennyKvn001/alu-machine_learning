#!/usr/bin/env python3
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Load data
lib = np.load("pca.npz")
data = lib["data"]
labels = lib["labels"]

# Center the data by subtracting the mean
data_means = np.mean(data, axis=0)
norm_data = data - data_means

# Perform Singular Value Decomposition (SVD)
_, _, Vh = np.linalg.svd(norm_data)

# Compute the PCA data using the first three principal components
pca_data = np.matmul(norm_data, Vh[:3].T)

# Define a color map for different Iris species
colors = ["r", "g", "b"]
species = np.unique(labels)

# Plot the PCA data in 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")

# Scatter plot for each Iris species
for i, specie in enumerate(species):
    ax.scatter(
        pca_data[labels == specie, 0],
        pca_data[labels == specie, 1],
        pca_data[labels == specie, 2],
        c=colors[i],
        label=specie,
    )

# Set plot labels and title
ax.set_xlabel("Principal Component 1")
ax.set_ylabel("Principal Component 2")
ax.set_zlabel("Principal Component 3")
ax.set_title("3D PCA of Iris Dataset")

# Show legend
ax.legend()

# Show the plot
plt.show()
