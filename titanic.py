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

train = train.drop(['Cabin', 'Ticket'], axis=1)
test = test.drop(['Cabin', 'Ticket'], axis=1)

train.info()

train[['Age','Survived']]

for row in data:
    row['Title'] = row.Name.str.extract('([A-Za-z]+)\.')
pd.crosstab(train['Title'],train['Sex'])

data

train.head()

for row in data:
    row['Title'] = row['Title'].replace(['Lady', 'Countess','Capt', 'Col',\
 	'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')

    row['Title'] = row['Title'].replace('Mlle', 'Miss')
    row['Title'] = row['Title'].replace('Ms', 'Miss')
    row['Title'] = row['Title'].replace('Mme', 'Mrs')
    
train[['Title', 'Survived']].groupby(['Title'], as_index=False).mean()

title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Rare": 5}
for row in data:
    row['Title'] = row['Title'].map(title_mapping)
    row['Title'] = row['Title'].fillna(0)

train.head()

train = train.drop(['Name','PassengerId','Ticket','Cabin'], axis=1)

test = test.drop(['Name','PassengerId','Ticket','Cabin'], axis=1)

train.info()

for row in data:
    row['Sex'] = row['Sex'].map( {'female': 1, 'male': 0} ).astype(int)


train.head()

test.head()

train = pd.get_dummies(train, columns=['Sex'])
test = pd.get_dummies(test, columns=['Sex'])

test.head()

train['AgeBand'] = pd.cut(train['Age'], 5)
train[['AgeBand', 'Survived']].groupby(['AgeBand'], as_index=False).mean().sort_values(by='AgeBand', ascending=True)

train = pd.get_dummies(train, columns=['AgeBand'])
train.head()

pd.cut(train['Fare'],100)