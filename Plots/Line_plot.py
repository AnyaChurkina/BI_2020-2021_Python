import matplotlib.pyplot as plt
import numpy as np

# Line plot with plt
x = np.arange(-np.pi, 6*np.pi, 0.1)  # data generation
sin_function, cos_function = np.sin(x), np.cos(x)  # second and third data generation

plt.plot(x, sin_function, color="green", alpha=.7,  linewidth=2, linestyle="-", label="sine")  # line for sine function
plt.plot(x, cos_function, color="orange", linewidth=2, linestyle="--", label="cosine")  # line for cosine function
plt.legend(loc='upper left')
plt.title('Line plot for BI Python course')
plt.grid(alpha=.5)
plt.show()
