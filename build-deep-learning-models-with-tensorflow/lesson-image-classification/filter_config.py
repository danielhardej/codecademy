import tensorflow as tf

print("\n\nModel with 8 filters:")

model = tf.keras.Sequential()
model.add(tf.keras.Input(shape=(256, 256, 1)))

#Adds a Conv2D layer with 8 filters, each size 3x3:
model.add(tf.keras.layers.Conv2D(16, 7, activation="relu"))
model.summary()
