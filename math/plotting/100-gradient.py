#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)

x = np.random.randn(2000) * 10
y = np.random.randn(2000) * 10
z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))

# Create scatter plot
plt.scatter(x, y, c=z, cmap="terrain")


cbar = plt.colorbar()
cbar.set_label("elevation (m)", fontsize="small")


plt.xlabel("x coordinate (m)", fontsize="small")
plt.ylabel("y coordinate (m)", fontsize="small")
plt.title("Mountain Elevation", fontsize="small")


plt.show()
