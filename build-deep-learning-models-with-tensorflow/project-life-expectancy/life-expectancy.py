# The World Health Organization (WHO)’s Global Health Observatory (GHO) data repository
# tracks life expectancy for countries worldwide by following health status and many
# other related factors.
#
# Although there have been a lot of studies undertaken in the past on factors affecting
# life expectancy considering demographic variables, income composition, and mortality
# rates, it was found that the effects of immunization and human development index
# were not taken into account.
#
# The dataset covers a variety of indicators for all countries from 2000 to 2015 including:
# immunization factors
# mortality factors
# economic factors
# social factors
# other health-related factors
#
# Ideally, this data will eventually inform countries concerning which factors to
# change in order to improve the life expectancy of their populations. If we can
# predict life expectancy well given all the factors, this is a good sign that there
# are some important patterns in the data. Life expectancy is expressed in years,
# and hence it is a number. This means that in order to build a predictive model
# one needs to use regression.
#
# In this project, you will design, train, and evaluate a neural network model
# performing the task of regression to predict the life expectancy of countries using
# this dataset.

import pandas as pd
import tensorflow as tf
from tensorflow.keras.layers import InputLayer
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer

tf.random.set_seed(42)

### Data loading and observing ###
dataset = pd.read_csv('life_expectancy.csv')
print(dataset.head())
print(dataset.describe())

dataset = dataset.drop(['Country'], axis=1)
print(dataset.head())
print(dataset.describe())

# choose the final column for the labels
labels = dataset.iloc[:,-1]
# choose features from the first column to the last column (but not including it!)
features = dataset.iloc[:,0:-1]

### Data Preprocessing ###
#one-hot encoding for categorical variables
features = pd.get_dummies(features)
# Split  data into training set and test sets
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.33, random_state=42)
# standardize/normalize numerical features
numerical_features = features.select_dtypes(include=['float64', 'int64'])
numerical_columns = numerical_features.columns
ct = sklearn.compose.ColumnTransformer([('only numeric', StandardScaler(), numerical_columns)], remainder='passthrough')
features_train_scaled = ct.fit_transform(features_train)
features_test_scaled = ct.transform(features_test)

### Building the model ###
my_model = tf.keras.models.Sequential()
tf.keras.layers.InputLayer
input = InputLayer(input_shape=(features.shape[1],))
my_model.add(input)
my_model.add(Dense(128, activation='relu'))
my_model.add(Dense(1))
print(my_model.summary())

### Initialize the optimizer and compile the model ###
opt = Adam(learning_rate=0.01)
my_model.compile(loss='mse', metrics='mae', optimizer=opt)
my_model.fit(features_train_scaled, labels_train, epochs=40, batch_size=1,verbose=1)

res_mse, res_mae = my_model.evaluate(features_test_scaled, labels_test, verbose=0)

print("Final loss (RMSE): "  +  res_mse)
print("MAE: " + res_mae)
