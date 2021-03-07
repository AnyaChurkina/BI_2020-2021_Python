from pandas import read_csv


#  Task 2 (data subset)
train = read_csv("https://raw.githubusercontent.com/Serfentum/bf_course/master/"
                 "14.pandas/train.csv")

new_train = train[train["matches"] > train["matches"].mean()]

train[train["matches"] > train["matches"].mean()][['pos', 'reads_all',
                                                   'mismatches', 'deletions',
                                                   'insertions']]. \
    to_csv('train_part.csv')
