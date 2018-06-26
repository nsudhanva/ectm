# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('engine_data_1.csv')
X = dataset.iloc[:, 2:11].values

# Encoding categorical data
X[5] = X[5] * 1
X[6] = X[6] * 1
X[7] = X[7] * 1
X[8] = X[8] * 1

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_test = sc.fit_transform(X)

# Importing the Keras libraries and packasges
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model
from keras.models import model_from_json

# Initialising the ANN
#classifier = load_model('sweg.h5')

json_file = open('classifier.json', 'r')
classifier_json = json_file.read()
json_file.close()

classifier_model = model_from_json(classifier_json)

classifier_model.load_weights("classifier_weight.h5")

classifier_model = load_model('classifier_weight.hdf5')

# Predicting the Test set results
y_pred = classifier_model.predict_classes(X_test)
