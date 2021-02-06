import numpy as np
import matplotlib.pyplot as plt
from random import randint


def midpoint(p, q):
    return [(p[0] + q[0]) / 3, (p[1] + q[1]) / 3]


side = [(0, 1), (1, 0), (1, 2), (2, 1),
        (0, 0), (2, 0), (0, 2), (2, 2)]

N = 1000000
x = np.zeros(N)
y = np.zeros(N)

for i in range(1, N):
    k = randint(0, 7)
    x[i], y[i] = midpoint(side[k], (x[i - 1], y[i - 1]))

plt.figure(figsize=(15, 10))
plt.scatter(x, y, color="lightpink", alpha=0.7)
plt.title("Sierpinski carpet")
plt.savefig("Sierpinski_carpet.png")
plt.show()
