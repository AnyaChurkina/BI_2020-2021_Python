import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Line plot with plt

# data generation
x = np.arange(-np.pi, 6*np.pi, 0.1)

# second and third data generation
sin_function, cos_function = np.sin(x), np.cos(x)

plt.figure(figsize=(12, 9))
plt.plot(x, sin_function, color="green", alpha=.7,  linewidth=2,
         linestyle="-", label="sine")  # line for sine function
plt.plot(x, cos_function, color="orange", linewidth=2,
         linestyle="--", label="cosine")  # line for cosine function
plt.legend(loc='upper left')
plt.title('Line plot for BI Python course(Matplotlib)')
plt.grid(alpha=.5)
plt.savefig("Matplotlib line plot.png")
plt.close()

# Line plot with sns
iris = sns.load_dataset('iris')  # Load dataset from 'seaborn-data' repository

plt.figure(figsize=(12, 9))
sns.lineplot(data=iris, x="sepal_length", y="sepal_width",
             hue="species", style="species")
plt.title('Line plot for BI Python course(Seaborn)')
# Warning! This graph looks horrible :)

plt.savefig("Seaborn line plot.png")
