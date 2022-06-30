# In this lesson, we will learn how neural networks can be applied to image classification.
# To do this, we will be using convolutional layers: layers designed to process image data by
# focusing on local relationships between features.
# #
# Pneumonia, the infection of lung tissue, is responsible for over two and a half million deaths
# worldwide. A radiologist’s diagnosis is often critical for the discovery and treatment of pneumonia.
# However, these doctors are often in short supply.
# #
# In this lesson, we will train a Convolutional Neural Network (CNN) to automatically
# classify chest X-rays, showcasing the potential for deep learning in medical domains.

import tensorflow as tf

model = tf.keras.Sequential()

#Add an input layer that will expect grayscale input images of size 256x256:
model.add(tf.keras.Input(shape=(256, 256)))

#Use a Flatten() layer to flatten the image into a single vector:
model.add(tf.keras.layers.Flatten())

model.add(tf.keras.layers.Dense(100,activation="relu"))
model.add(tf.keras.layers.Dense(50,activation="relu"))
model.add(tf.keras.layers.Dense(2,activation="softmax"))

#Print model information:
model.summary()
