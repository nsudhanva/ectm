# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Importing the dataset
dataset = pd.read_csv('../../data/engine_data_error_final.csv')

X = dataset.loc[:, ['egt']].values
y = dataset.loc[:, ['fp_egt']].values

# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, shuffle=False)

# Fitting Simple Linear Regression to the Training set
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the results
y_pred = regressor.predict(X_test)
y_pred = y_pred / 100
y_pred[y_pred > 1] = 1
y_pred[y_pred < 0] = 0

# Saving the model
with open('slr_egt.pkl', 'wb') as f:
    pickle.dump(regressor, f)
    