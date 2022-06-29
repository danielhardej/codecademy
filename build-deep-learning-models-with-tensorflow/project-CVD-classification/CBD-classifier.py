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
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from collections import Counter
from sklearn.compose import ColumnTransformer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, InputLayer
from sklearn.metrics import classification_report
from tensorflow.keras.utils import to_categorical
import numpy as np

### Loading the data ###
data = pd.read_csv("heart_failure.csv")
print(data.info())
print(Counter(data["death_event"]))

features = data[['age','anaemia','creatinine_phosphokinase','diabetes','ejection_fraction','high_blood_pressure','platelets','serum_creatinine','serum_sodium','sex','smoking','time']]
labels = data["death_event"]

features = pd.get_dummies(features)

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.33, random_state=42)

ct = ColumnTransformer([('numeric', StandardScaler(), ['age','creatinine_phosphokinase','ejection_fraction','platelets','serum_creatinine','serum_sodium','time'])], remainder='passthrough')

features_train_scale = ct.fit_transform(features_train)
features_test_scale = ct.transform(features_test)


### Prepare labels for classification ###
le = LabelEncoder()
labels_train = le.fit_transform(labels_train.astype(str))
labels_test = le.transform(labels_test.astype(str))

labels_train = to_categorical(labels_train)
labels_test = to_categorical(labels_test)


### Design the model ###
