# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('../../data/engine_data_1.csv')
X = dataset.iloc[:, 0:9].values
y = dataset.iloc[:, [11]].values

# Encoding categorical data
y = y * 1

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_0 = LabelEncoder()
X[:, 0] = labelencoder_X_0.fit_transform(X[:, 0])
labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
onehotencoder = OneHotEncoder(categorical_features = [0, 1])
X = onehotencoder.fit_transform(X).toarray()

categories = [0, 1]
dummies = []
dummies_sum = 0

for category in categories:
    dummies_sum += (dataset.iloc[:, category].unique().size) * category
    dummies.append(dummies_sum)

X = np.delete(X, dummies, 1)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

engine_nos = dataset.iloc[0:200, 0].values
time_test = X_test[0:200, 46]

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting Random Forest Classification to the Training set
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred_prob = classifier.predict_proba(X_test)

y_pred_prob_y = y_pred_prob[0:200, :1].ravel()

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

accuracy = classifier.score(X_test, y_test)

from sklearn.metrics import classification_report

report = classification_report(y_test, y_pred)

fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(111)

#plt.xticks(np.arange(len(df_time_group.index)), df_time_group.index, rotation=30, fontsize=8)
plt.title('Probability of N1 failure', fontsize=25)
plt.xlabel('Probability', fontsize=20)
plt.ylabel('Age (in months)', fontsize=20)
plt.scatter(y_pred_prob_y, time_test, marker='o', color='r')

#for i, y in enumerate(engine_nos):
#    ax.annotate(y, (y_pred_prob_y[i], time_test[i]), fontsize=10)

plt.show()



