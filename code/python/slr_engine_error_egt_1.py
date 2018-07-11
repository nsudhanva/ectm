# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pickle
import csv

# Importing the dataset
dataset = pd.read_csv('../../data/engine_data_error_final_1.csv')

X_data = dataset.loc[:, ['month', 'egt']]
X = X_data.values

# Encoding categorical data
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding dummy variable trap
categories = [0]
dummies = []
dummies_sum = 0

for category in categories:
    dummies_sum += (dataset.iloc[:, category].unique().size) * category
    dummies.append(dummies_sum)

X = np.delete(X, dummies, 1)

# Loading and fitting the regression model
with open('slr_egt.pkl', 'rb') as f:
    regressor = pickle.load(f)

# Predicting the results
y_pred = regressor.predict(X)
y_pred[y_pred > 100] = 100
y_pred[y_pred < 0] = 0

# Writing values to a file
dataset['fp_egt'] = list(y_pred.astype(int).ravel())
dataset.to_csv('../../data/engine_data_error_final_1.csv', index=False)