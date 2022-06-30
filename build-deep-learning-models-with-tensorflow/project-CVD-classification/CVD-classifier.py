# In this project, you will use a dataset from Kaggle to predict the survival of
# patients with heart failure from serum creatinine and ejection fraction,
# and other factors such as age, anemia, diabetes, and so on.
#
# Cardiovascular diseases (CVDs) are the number 1 cause of death globally, taking
# an estimated 17.9 million lives each year, which accounts for 31% of all deaths
# worldwide. Heart failure is a common event caused by CVDs, and this dataset
# contains 12 features that can be used to predict mortality by heart failure.
#
# Most cardiovascular diseases can be prevented by addressing behavioral risk factors
# such as tobacco use, unhealthy diet and obesity, physical inactivity,
# and harmful alcohol use using population-wide strategies.
#
# People with cardiovascular disease or who are at high cardiovascular risk
# (due to the presence of one or more risk factors such as hypertension, diabetes,
# hyperlipidemia, or already established disease) need early detection and management
# wherein a machine learning model can be of great help.

import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from collections import Counter
from sklearn.compose import ColumnTransformer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, InputLayer
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import classification_report
from tensorflow.keras.utils import to_categorical
import numpy as np

tf.random.set_seed(42) #for the reproducibility of results

NUM_LAYERS = 1
NUM_NEURONS = 12
NUM_EPOCHS = 100
BATCH_SIZE = 16

### Loading the data ###
data = pd.read_csv("heart_failure.csv")
print(data.info())
print(Counter(data["death_event"]))

features = data[['age','anaemia','creatinine_phosphokinase','diabetes','ejection_fraction','high_blood_pressure','platelets','serum_creatinine','serum_sodium','sex','smoking','time']]

labels = data["death_event"]

features = pd.get_dummies(features)

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.33, random_state=42)

ct = ColumnTransformer([('numeric', StandardScaler(), ['age','creatinine_phosphokinase','ejection_fraction','platelets','serum_creatinine','serum_sodium','time'])])

features_train_scale = ct.fit_transform(features_train)
features_test_scale = ct.transform(features_test)


### Prepare labels for classification ###
le = LabelEncoder()
labels_train = le.fit_transform(labels_train.astype(str))
labels_test = le.transform(labels_test.astype(str))

labels_train = to_categorical(labels_train)
labels_test = to_categorical(labels_test)

### Design the model ###
model = Sequential()
# create input layer
model.add(InputLayer(input_shape=(features_train_scale.shape[1],)))
# create hidden layers
model.add(Dense(NUM_NEURONS, activation='relu'))
# create output layer
model.add(Dense(2, activation='softmax'))
#opt = Adam(learning_rate=0.1)
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


### Train and evaluate the model ###
model.fit(features_train_scale, labels_train, epochs=NUM_EPOCHS, batch_size=BATCH_SIZE, verbose=1)
loss, acc = model.evaluate(features_test_scale, labels_test, verbose=0)

print("Loss: ", loss)
print("Accuracy: ", acc)
print()
print(model.summary())

### Generate classification report ###
estimate_vals = model.predict(features_test_scale)
estimate_vals = np.argmax(estimate_vals, axis=1)
true_vals = np.argmax(labels_test, axis=1)

print()
print(classification_report(true_vals, estimate_vals))

#r2score = r2_score(labels_test, estimate_vals)
#print("R2 score: " + str(r2score))

# NOTE TO SELF: I tried using R2 score here, as I did in another project; however, it turns out that R2 score is not
# a good measure to assess the fit for a binary classification like we had here.
# Instead, R2 is suitable for is suitable for predicting continuous variable. See more here:
# https://stats.stackexchange.com/questions/273133/interpretation-of-r-squared-score-of-a-neural-network-for-classification
