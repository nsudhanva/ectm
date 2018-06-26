import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('engine_data.csv')

X = dataset.iloc[:, 2:7].values
y = dataset.iloc[:, 11].values

# Converting true false to 1s and 0s
y = y * 1

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)