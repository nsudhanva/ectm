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