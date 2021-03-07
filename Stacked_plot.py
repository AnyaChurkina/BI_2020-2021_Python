from matplotlib import pyplot as plt
from pandas import read_csv


#  Task 1 (distribution stacked bar plot)
train = read_csv("https://raw.githubusercontent.com/Serfentum/bf_course/master/"
                 "14.pandas/train.csv")

train['A_fraction'] = train['A_fraction'] * 100
train['T_fraction'] = train['T_fraction'] * 100
train['G_fraction'] = train['G_fraction'] * 100
train['C_fraction'] = train['C_fraction'] * 100

train[['pos', 'A_fraction', 'T_fraction', 'G_fraction', 'C_fraction']]. \
    plot.bar(x="pos", stacked=True)
plt.title("Frequency for each nucleotides per position")
plt.xlabel("Position")
plt.ylabel("Frequency")
plt.show()
# plt.savefig("Stacked bar plot.png")
