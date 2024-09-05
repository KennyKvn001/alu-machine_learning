#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

# Plot y as a solid red line with the x-axis ranging from 0 to 10
plt.plot(range(11), y, "r-")

plt.xlim(0, 10)

plt.show()
