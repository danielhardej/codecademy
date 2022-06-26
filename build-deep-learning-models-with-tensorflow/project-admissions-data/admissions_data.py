import app
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow	import keras
from tensorflow.keras.layers import InputLayer
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras import layers
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.metrics import r2_score

tf.random.set_seed(42)

### Set Hyperparameters ###
N_LAYERS = 3
N_NEURONS = 64
BATCH_SIZE = 1
N_EPOCHS = 50
L_RATE=0.01

### Data loading and observing ###
dataset = pd.read_csv('admissions_data.csv')
print(dataset.head())
print(dataset.describe())

labels = dataset.iloc[:,-1]
features = dataset.iloc[:,0:-1]
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.33, random_state=42)

numerical_features = features.select_dtypes(include=['float64', 'int64'])
numerical_columns = numerical_features.columns
ct = ColumnTransformer([('only numeric', StandardScaler(), numerical_columns)], remainder='passthrough')
features_train_scaled = ct.fit_transform(features_train)
features_test_scaled = ct.transform(features_test)

### Building the model ###
my_model = tf.keras.models.Sequential()
input = InputLayer(input_shape=(features.shape[1],))
my_model.add(input)
for l in range(N_LAYERS):
  my_model.add(Dense(N_NEURONS, activation='relu'))
my_model.add(Dense(1))
#print(my_model.summary())

opt = Adam(learning_rate=L_RATE)
my_model.compile(loss='mse', metrics='mae', optimizer=opt)
my_model.fit(features_train_scaled, labels_train, epochs=N_EPOCHS, batch_size=BATCH_SIZE, verbose=1)

res_mse, res_mae = my_model.evaluate(features_test_scaled, labels_test, verbose=0)

print("Final loss (RMSE): "  +  str(res_mse))
print("MAE: " + str(res_mae))

# Do extensions code below
# if you decide to do the Matplotlib extension, you must save your plot in the directory by uncommenting the line of code below

# fig.savefig('static/images/my_plots.png')
