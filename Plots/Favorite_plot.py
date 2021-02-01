import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')  # Load dataset from 'seaborn-data' repository

# Or define dataset from URL with using pandas:
# import pandas as pd
# iris = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

sns.set_style('whitegrid')
sns.pairplot(iris, hue='species', palette='Set1')

plt.savefig("Iris pair plot.png")
