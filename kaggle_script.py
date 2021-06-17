import pandas as pd
import numpy as np

#reading files
train = pd.read_csv('train.csv')
train_labels = train['target']
train = train.drop(columns='target')
test = pd.read_csv('test.csv')
# print(train.head())
# print(train_labels.head())
# print(test.head())

#DEA
train_types = train.dtypes
train_labels_types = train_labels.dtypes
train_null = train.isnull().sum()
labels_null = train_labels.isnull().sum()
print(train_null)
print('\n')
print(labels_null)