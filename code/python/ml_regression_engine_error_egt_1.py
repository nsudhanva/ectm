# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.externals import joblib
import pickle

# Importing the dataset
dataset = pd.read_csv('../../data/engine_data_error_egt_1.csv')
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

# Loading and fitting the regression model
with open('mlr_egt.pkl', 'rb') as f:
    regressor = pickle.load(f)
    
y_pred = regressor.predict(X)

y_pred[y_pred > 1] = 1
y_pred[y_pred < 0] = 0

# Visualising the results

normal_dataset = pd.read_csv('../../data/engine_data_normal.csv')
y_normal = normal_dataset.loc[:, 'failure_prob'].values
y_normal = y_normal / 100
y_normal[y_normal > 1] = 1

plt.plot(X_data['month'][0:60], y_normal[0:60], color = 'green', linestyle='-', marker='.', label='Age')
plt.plot(X_data['month'][0:60], y_pred[0:60], color = 'blue', linestyle='-', marker='.', label='Probability')
plt.axvline(x=np.where(y_pred==1)[0][0], color='red', label='Predicted Failure Month')
plt.axvline(x=np.where(y_normal==1)[0][0], color='orange', label='Normal Failure Month')        
plt.xticks(np.arange(0, 61, 2))
plt.yticks(np.arange(0, 1.05, 0.05))
plt.title('Age (in months) vs Probability of Failure')
plt.legend(loc='best')
plt.xlabel('Age (in months)')
plt.ylabel('Probability of Failure')
plt.show()

print('Engine will fail by month ' + str(np.where(y_pred==1)[0][0]) + '. It should have survived for ' + str(np.where(y_normal==1)[0][0]) + 'months.')