from pandas import read_csv
from statistics import mean

#  Task 2 (data subset)
train = read_csv("https://raw.githubusercontent.com/Serfentum/bf_course/"
                 "master/14.pandas/train.csv")


train[train["matches"] > mean(train["matches"])][['pos', 'reads_all',
                                                   'mismatches', 'deletions',
                                                   'insertions']]. \
    to_csv('train_part.csv')
