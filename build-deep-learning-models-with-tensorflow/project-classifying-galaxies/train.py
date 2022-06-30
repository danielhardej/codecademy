# In this project, you will build a neural network to classify deep-space galaxies.
# You will be using image data curated by Galaxy Zoo, a crowd-sourced project
# devoted to annotating galaxies in support of scientific discovery.
#
# You will identify “odd” properties of galaxies. The data falls into four classes:
#
# [1,0,0,0] - Galaxies with no identifying characteristics.
# Three regular galaxies. Each has a bright center, surrounded by a cloud of stars.
#
# [0,1,0,0] - Galaxies with rings.
# Three ringed galaxies. Each has a bright center, surrounded by a ring of stars.
#
# [0,0,1,0] - Galactic mergers.
# Three photos of galaxies. Each contains two bright orbs surrounded by clouds. These images show galaxies in the process of merging.
#
# [0,0,0,1] - “Other,” Irregular celestial bodies.

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from utils import load_galaxy_data
from visualize import visualize_activations
import app

### Set hyperparams ###
NUM_EPOCHS = 40
BATCH_SIZE = 1
LEARN_RATE = 0.01

### Loading the data ###
input_data, labels = load_galaxy_data()
print(input_data.shape)
print(labels.shape)

features_train, features_validation, labels_train, labels_validation = train_test_split(input_data, labels, test_size=0.20, stratify=labels, shuffle=True, random_state=222)

idg = ImageDataGenerator(rescale = 1.0/255)

### Prepare labels for classification ###
training_data_iterator = idg.flow(features_train, labels_train, batch_size=BATCH_SIZE)
validation_data_iterator = idg.flow(features_validation, labels_validation, batch_size=BATCH_SIZE)

### Design the model ###
# create model and input layer
model = tf.keras.Sequential()
model.add(tf.keras.Input(shape = input_data.shape[1:]))
# add convolutional layers
model.add(tf.keras.layers.Conv2D(8, 3, strides=2, activation="relu"))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(tf.keras.layers.Conv2D(8, 3, strides=2, activation="relu"))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(16, activation = "relu"))
# add output layer that outputs 4 features/classes: “Normal”,”Ringed”,”Merger”,”Other”
model.add(tf.keras.layers.Dense(4, activation="softmax"))

model.summary()

model.compile(
            optimizer = tf.keras.optimizers.Adam(learning_rate=LEARN_RATE),
            loss = tf.keras.losses.CategoricalCrossentropy(),
            metrics = [tf.keras.metrics.CategoricalAccuracy(), tf.keras.metrics.AUC()]
            )


### Train and evaluate the model ###
model.fit(
       training_data_iterator,
       steps_per_epoch = len(training_data_iterator)/BATCH_SIZE,
       epochs = NUM_EPOCHS,
       validation_data = validation_data_iterator,
       validation_steps = len(validation_data_iterator)/BATCH_SIZE
)


visualize_activations(model, validation_data_iterator)
