# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.linear_model import LinearRegression
import pickle
import csv
import generate_final_data # this is to generate data

# Importing the dataset
dataset = pd.read_csv('../../data/engine_final.csv')

# ==================================
#               noise
# ==================================

X_noise_data = dataset.iloc[:, 3:4]
X_noise = X_noise_data.values

# Loading and fitting the regression model
with open('slr_noise.pkl', 'rb') as f:
    regressor = pickle.load(f)

# Predicting the results
y_pred_noise = regressor.predict(X_noise)
y_pred_noise[y_pred_noise > 100] = 100
y_pred_noise[y_pred_noise < 0] = 0

dataset['fp_noise'] = list(y_pred_noise.astype(int).ravel())

# ==================================
#               EGT
# ==================================

X_egt_data = dataset.loc[:, ['egt']]
X_egt = X_egt_data.values

# Loading and fitting the regression model
with open('slr_egt.pkl', 'rb') as f:
    regressor = pickle.load(f)

# Predicting the results
y_pred_egt = regressor.predict(X_egt)
y_pred_egt[y_pred_egt > 100] = 100
y_pred_egt[y_pred_egt < 0] = 0

# Writing values to a file
dataset['fp_egt'] = list(y_pred_egt.astype(int).ravel())

# ==================================
#               FF
# ==================================

X_ff_data = dataset.loc[:, ['ff']]
X_ff = X_ff_data.values

# Loading and fitting the regression model
with open('slr_ff.pkl', 'rb') as f:
    regressor = pickle.load(f)

# Predicting the results
y_pred_ff = regressor.predict(X_ff)
y_pred_ff[y_pred_ff > 100] = 100
y_pred_ff[y_pred_ff < 0] = 0

dataset['fp_ff'] = list(y_pred_ff.astype(int).ravel())

# ==================================
#               N1
# ==================================

X_n1_data = dataset.loc[:, ['n1']]
X_n1 = X_n1_data.values

# Loading and fitting the regression model
with open('slr_n1.pkl', 'rb') as f:
    regressor = pickle.load(f)

# Predicting the results
y_pred = regressor.predict(X)
y_pred[y_pred > 100] = 100
y_pred[y_pred < 0] = 0

dataset['fp_n1'] = list(y_pred.astype(int).ravel())

# ==================================
#               N2
# ==================================




dataset.to_csv('../../data/engine_final.csv', index=False)
