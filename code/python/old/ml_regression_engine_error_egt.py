# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pickle

# Importing the dataset
dataset = pd.read_csv('../../data/engine_data_error_egt.csv')
X_data = dataset.iloc[:, 1:9]
y_data = dataset.iloc[:, [16]]

X = X_data.values
y = y_data.values

y = y/100

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

# Splitting dataset into Training and Test Set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, shuffle = False)

# Fitting Multiple Linear Regression to the Training Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test Set results
y_pred = regressor.predict(X)
y_pred[y_pred > 1] = 1
y_pred[y_pred < 0] = 0
# y_pred = y_pred.ravel()
# y_p = np.abs(y_pred) / 100

# Saving the model
with open('mlr_egt.pkl', 'wb') as f:
    pickle.dump(regressor, f)

# Visualising the results
# First Observation
plt.plot(X_data['month'][0:60], y_test[0:60], color = 'red')
plt.plot(X_data['month'][0:60], y_pred[0:60], color = 'blue')
plt.xticks(np.arange(0, 61, 2))
plt.yticks(np.arange(0, 1.05, 0.05))
plt.title('Age (in months) vs Probability of Failure')
plt.xlabel('Age (in months)')
plt.ylabel('Probability of Failure')
plt.show()
