# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('engine_data_1.csv')
X = dataset.iloc[:, 2:11].values

y_test = dataset.iloc[:, [11]].values


encode = lambda x: x * 1
X['EGT Normal'] = X['EGT Normal'].apply(encode)
X['Fuel Flow Normal'] = X['Fuel Flow Normal'].apply(encode)
X['N1 Normal'] = X['N1 Normal'].apply(encode)
X['N2 Normal'] = X['N2 Normal'].apply(encode)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_test = sc.fit_transform(X)

# Importing the Keras libraries and packasges
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model

# Initialising the ANN
classifier = load_model('classifier.h5')

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
