import numpy as np
import matplotlib.pyplot as plt
from random import randint


def midpoint(p, q):
    return [0.5*(p[0] + q[0]), 0.5*(p[1] + q[1])]


corner = [(0, 0), (0.5, np.sqrt(3) / 2), (1, 0)]

N = 100000
x = np.zeros(N)
y = np.zeros(N)

for i in range(1, N):
    k = randint(0, 2)
    x[i], y[i] = midpoint(corner[k], (x[i - 1], y[i - 1]))

plt.figure(figsize=(15, 10))
plt.scatter(x, y, color="rosybrown")
plt.title("Sierpinski triangle")
plt.savefig("Sierpinski_triangle_v2.png")
plt.show()
