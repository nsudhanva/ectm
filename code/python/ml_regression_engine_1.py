# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.externals import joblib

# Importing the dataset
dataset = pd.read_csv('../../data/engine_data_1.csv')
X = dataset.iloc[:, 1:9]
y = dataset.iloc[:, [16]]

# Splitting the dataset manually
X_train = X.iloc[0:1800, :]
X_test = X.iloc[1800:2400, :]

y_train = y.iloc[0:1800, :].values
y_test = y.iloc[1800:2400, :].values

# Encoding categorical data
X_train_encode = X_train.values
X_test_encode = X_test.values

labelencoder_X_train = LabelEncoder()
X_train_encode[:, 0] = labelencoder_X_train.fit_transform(X_train_encode[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X_train_encode = onehotencoder.fit_transform(X_train_encode).toarray()

labelencoder_X_test = LabelEncoder()
X_test_encode[:, 0] = labelencoder_X_test.fit_transform(X_test_encode[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X_test_encode = onehotencoder.fit_transform(X_test_encode).toarray()

# Avoiding dummy variable trap
categories = [0]
dummies = []
dummies_sum = 0

for category in categories:
    dummies_sum += (dataset.iloc[:, category].unique().size) * category
    dummies.append(dummies_sum)

X_train_encode = np.delete(X_train_encode, dummies, 1)
X_test_encode = np.delete(X_test_encode, dummies, 1)


# Fitting Multiple Linear Regression to the Training Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train_encode, y_train)

# Predicting the Test Set results
y_pred = regressor.predict(X_test_encode)
y_pred = y_pred.ravel() 
y_p = np.abs(y_pred) / 100

# Saving the model
#joblib.dump(regressor, 'multiple_reg_1.pkl')

# Visualising the results

# First Observation
plt.plot(X_test['month'][0:24], y_p[0:24], color = 'blue')
plt.xticks(np.arange(0, 25, 1))
plt.yticks(np.arange(0, 1.05, 0.05))
plt.title('Age (in months) vs Probability of Failure')
plt.xlabel('Age (in months)')
plt.ylabel('Probability of Failure')
plt.show()

# All Observations
plt.figure(figsize=(100, 100))
plt.plot(X_test['month'], y_p, color = 'blue')
plt.xticks(np.arange(0, 24, 1))
plt.yticks(np.arange(0, 1.05, 0.05))
plt.title('Age (in months) vs Probability of Failure')
plt.xlabel('Age (in months)')
plt.ylabel('Probability of Failure')
plt.show()
