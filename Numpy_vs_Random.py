import numpy as np
import random
import time
import matplotlib.pyplot as plt


numpy_time = []
random_time = []
array_size = range(1, 10000)  # define size of arrays


def np_uniform(s):
    numpy_distribution = np.random.uniform(0, 1, s)
    return numpy_distribution


def random_uniform(s):
    random_distribution = list(random.uniform(0, 1) for _ in range(s))
    return random_distribution


for size in array_size:
    # Counting the time to create numpy uniform distributions several sizes
    start_numpy_time = time.time()
    np_uniform(size)
    numpy_time.append(time.time() - start_numpy_time)

    # Counting the time to create random uniform distributions several sizes
    start_random_time = time.time()
    random_uniform(size)
    random_time.append(time.time() - start_random_time)

plt.figure(figsize=(15, 10))
plt.plot(array_size, numpy_time, color="green", alpha=.7,  linewidth=2,
         linestyle="-", label="Numpy uniform distribution")
plt.plot(array_size, random_time, color="orange", linewidth=2, linestyle="--",
         label="Random uniform distribution")
plt.ylabel('Time(s)')
plt.xlabel('Array size')
plt.legend(loc='upper left')
plt.grid(alpha=.5)
plt.savefig('Numpy_vs_Random.png')
plt.show()
