"""
It is very easy python script to plot sequence length distribution of fasta file with using Biopython

To paint use:
    python3 distribution_plot.py <absolut path to fasta file>
"""

# Modules
import sys
from Bio import SeqIO
import pylab
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

input_arguments = sys.argv
if input_arguments[-1].endswith(".fasta"):
    file_to_paint = input_arguments.pop()
else:
    raise FileNotFoundError("Input file is not defined")

print("Start painting")

# Count the length of sequences
sequence_length = [len(reads) for reads in SeqIO.parse(file_to_paint, "fasta")]

# Plot
# Histogram with pylab
plt.figure(figsize=(20, 15))  # determination of figure size

plt.subplot(2, 2, 1)  # plot upper left graph
pylab.hist(sequence_length, edgecolor='black', linewidth=1.2, bins=20)
pylab.ylabel("Number of sequences")
pylab.xlabel("Sequence length (bp)")
pylab.title('Length distribution histogram with pylab')

# Distribution plot with seaborn
plt.subplot(2, 2, 2)  # plot upper right graph
plt.ylabel("Number of sequences")
plt.xlabel("Sequence length (bp)")
plt.title('Length distribution histogram with seaborn and pyplot')
sns.histplot(sequence_length, kde=True, bins=20)

# Density plot
plt.subplot(2, 2, 3)  # plot lower left graph
plt.ylabel("Density")
plt.xlabel("Sequence length (bp)")
plt.title('Density plot with pyplot')
sns.kdeplot(sequence_length, fill=True, alpha=.2)

# Distribution plot like FastQC
length = list(Counter(sorted(sequence_length)).keys())
count = list(Counter(sorted(sequence_length)).values())

plt.subplot(2, 2, 4)  # plot lower right graph
plt.plot(length, count, color="red")
plt.xlabel("Sequence length (bp)")
plt.ylabel("Number of sequences")
plt.title("Sequence length distribution plot like FastQC")
plt.grid(axis='y')
plt.savefig("Sequence length distribution plot.png")
plt.close()

print("Painting is done")
