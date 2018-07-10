# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import csv

# Importing the dataset
dataset = pd.read_csv('../../data/engine_data_error_final_1.csv')

X_data = dataset.iloc[:, 3:4]
X = X_data.values

# Loading and fitting the regression model
with open('slr_noise.pkl', 'rb') as f:
    regressor = pickle.load(f)

# Predicting the results
y_pred = regressor.predict(X)
y_pred[y_pred > 100] = 100
y_pred[y_pred < 0] = 0

dataset['fp_noise'] = list(y_pred.astype(int).ravel())
dataset.to_csv('../../data/engine_data_error_final_1.csv', index=False)