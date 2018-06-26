# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('engine_data_1.csv')
X = dataset.iloc[:, 2:7].values
y = dataset.iloc[:, [11]].values

# Encoding categorical data
y = y * 1

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Importing the Keras libraries and packasges
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model

# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
# classifier.add(Dense(output_dim = 2, init = "uniform", activation='relu', input_dim = 2))
classifier.add(Dense(activation="relu", input_dim=5, units=10, kernel_initializer="uniform"))

# Adding the second hidden layer
classifier.add(Dense(activation="relu", units=10, kernel_initializer="uniform"))

# Adding the output layer
classifier.add(Dense(activation="sigmoid", units=1, kernel_initializer="uniform"))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 100, nb_epoch = 100)

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

#classifier.save('classifier.h5') # creates a HDF5 file 'my_model.h5'

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

accuracy = (cm[0][0] + cm[1][1])/ 20000