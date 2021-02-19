import numpy as np
import random
import matplotlib.pyplot as plt


step_number = 1000  # define the number of steps

# define x and y coordinate
x = np.zeros(step_number)
y = np.zeros(step_number)

# walking...
for i in range(1, step_number):
    var = random.randint(1, 4)
    if var == 1:
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]
    elif var == 2:
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
    elif var == 3:
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    else:
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 1

plt.figure(figsize=(15, 10))
plt.scatter(x, y, color="teal", s=10, alpha=0.8)
plt.xlabel("X position")
plt.ylabel("Y position")
plt.title("Random walk")
plt.savefig("random_walk.png")
plt.show()
