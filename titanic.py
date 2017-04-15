# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 12:12:19 2017

@author: Varun
"""

import pandas as pd
import numpy as np

train_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
train = pd.read_csv(train_url)

test_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
test = pd.read_csv(test_url)

train.head()

train.describe()

data = [train, test]

data.head()

train.isnull().sum()

test.isnull().sum()

train.columns.values


print(train.info())

train.describe(include=['O'])

print(train[['Pclass','Survived']].groupby(['Pclass']).mean())

print(pd.crosstab(train['Pclass'], train['Survived']))

print(train[['Sex','Survived']].groupby(['Sex']).mean())

print(train[['SibSp','Survived']].groupby(['SibSp']).mean())


print(train[['Parch','Survived']].groupby(['Parch']).mean())

