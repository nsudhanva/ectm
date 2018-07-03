# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.externals import joblib

# Importing the dataset
dataset = pd.read_csv('engine_data1.csv')
X = dataset.iloc[:, 1:6]

# Splitting the dataset manually
X_train = X

# Encoding categorical data
X_train_encode = X_train.values

labelencoder_X_train = LabelEncoder()
X_train_encode[:, 0] = labelencoder_X_train.fit_transform(X_train_encode[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
#X_train_encode[:, 1] = labelencoder_X_train.fit_transform(X_train_encode[:, 1])
#onehotencoder = OneHotEncoder(categorical_features = [0, 1])
X_train_encode = onehotencoder.fit_transform(X_train_encode).toarray()


# Avoiding dummy variable trap
# Don't really have to do it manually in python
categories = [0]
dummies = []
dummies_sum = 0

for category in categories:
    dummies_sum += (dataset.iloc[:, category].unique().size) * category
    dummies.append(dummies_sum)

X_train_encode = np.delete(X_train_encode, dummies, 1)

#from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 0)

# Fitting Multiple Linear Regression to the Training Set
regressor = joblib.load('multiple_reg.pkl')

# Predicting the Test Set results
y_pred = regressor.predict(X_train_encode)

# Visualising the training set results
#plt.plot(X_test['month'][0:24], y_p[0:24], color = 'blue')
#plt.title('Age (in months) vs Probability of Failure (Training Set)')
#plt.xlabel('Age (in months)')
#plt.ylabel('Probability of Failure')
#plt.show()


