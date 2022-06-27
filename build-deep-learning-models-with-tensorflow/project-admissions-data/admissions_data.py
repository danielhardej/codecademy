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
N_LAYERS = 1
N_NEURONS = 64
BATCH_SIZE = 1
N_EPOCHS = 100
L_RATE=0.01
VAL_SPLT=0.2

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
h1 = my_model.fit(features_train_scaled, labels_train, epochs=N_EPOCHS, batch_size=BATCH_SIZE, verbose=1, validation_split=VAL_SPLT)

res_mse, res_mae = my_model.evaluate(features_test_scaled, labels_test, verbose=0)
predicted_values = my_model.predict(features_test_scaled)
r2score = r2_score(labels_test, predicted_values)

print()
print("Summary: ")
print("Number of layers: " + str(N_LAYERS))
print("Number of neurons: " + str(N_NEURONS))
print("Batch size: "  + str(BATCH_SIZE))
print("Number of epochs: " + str(N_EPOCHS))
print("Learning rate: " + str(L_RATE))
print("Validation split: " + str(VAL_SPLT))
print("R2 score: " + str(r2score))
print("Final loss (RMSE): "  +  str(res_mse))
print("MAE: " + str(res_mae))
# print(h1.history.keys())


fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax1.plot(h1.history['mae'])
ax1.plot(h1.history['val_mae'])
ax1.set_title('model mae')
ax1.set_ylabel('MAE')
ax1.set_xlabel('epoch')
ax1.legend(['train', 'validation'], loc='upper left')

  # Plot loss and val_loss over each epoch
ax2 = fig.add_subplot(2, 1, 2)
ax2.plot(h1.history['loss'])
ax2.plot(h1.history['val_loss'])
ax2.set_title('model loss')
ax2.set_ylabel('loss')
ax2.set_xlabel('epoch')
ax2.legend(['train', 'validation'], loc='upper left')

fig.tight_layout()
fig.savefig('static/images/my_plots.png')
