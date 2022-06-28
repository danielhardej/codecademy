# lesson on multi-class classification using air quality data
#
# in the dataset, amounts of the following partiiculates and pollutants and quanitified:
# 'PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene', 'AQI'
# these are treated as the features in the training and test sets
#
# air quality is then classified as one of the following:
# {'Very Poor': 1297, 'Poor': 1297, 'Moderate': 1297, 'Satisfactory': 1297, 'Severe': 1297, 'Good': 1297}
# these classes are treated as the labels in the training and test sets
#
# a neural net is created using a Keras Sequential model, with a ReLU activation function for the middle layer,
# and a softmax function at the output layer of 6 neurons, which classifies a datapint as one of the six classes
# listed above.
#
# the model is trained and compiled using categorical cross entropy and an Adam optimizer
#
# NB Sparse categorical cross-entropy can also be used to save time and memory in computation
# (Sparse categorical cross-entropy uses a single integer for a class, rather than a
# whole vector - useful when we have data with many classes to predict.)

import pandas as pd
from collections import Counter
from sklearn.preprocessing import LabelEncoder
import tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import  InputLayer
from tensorflow.keras.layers import  Dense
#your code here

train_data = pd.read_csv("air_quality_train.csv")
test_data = pd.read_csv("air_quality_test.csv")

#print columns and their respective types
print(train_data.info())
#print the class distribution
print(Counter(train_data["Air_Quality"]))
#extract the features from the training data
x_train = train_data[['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene', 'AQI']]
#extract the label column from the training data
y_train = train_data["Air_Quality"]
#extract the features from the test data
x_test = test_data[['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene', 'AQI']]
#extract the label column from the test data
y_test = test_data["Air_Quality"]

#encode the labels into integers
le = LabelEncoder()

#convert the integer encoded labels into binary vectors
y_train=le.fit_transform(y_train.astype(str))
y_test=le.transform(y_test.astype(str))

#convert the integer encoded labels into binary vectors
y_train = tensorflow.keras.utils.to_categorical(y_train, dtype = 'int64')
y_test = tensorflow.keras.utils.to_categorical(y_test, dtype = 'int64')

#design the model
model = Sequential()
model.add(InputLayer(input_shape=(x_train.shape[1],)))
model.add(Dense(10, activation='relu'))
model.add(Dense(6, activation='softmax'))

#compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
z
# alternatively, use Sparse categorical cross-entropy can also be used to save time and memory
# model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

#train and evaluate the model
model.fit(x_train, y_train, epochs = 30, batch_size = 16, verbose = 0)

#get additional statistics
y_estimate = model.predict(x_test)
y_estimate = np.argmax(y_estimate, axis = 1)
y_true = np.argmax(y_test, axis = 1)
print(classification_report(y_true, y_estimate))
