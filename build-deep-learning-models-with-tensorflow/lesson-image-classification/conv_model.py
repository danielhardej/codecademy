import tensorflow as tf

model = tf.keras.Sequential()


model.add(tf.keras.Input(shape=(256,256,1)))

#Add a Conv2D layer
# - with 2 filters of size 5x5
# - strides of 3
# - valid padding
model.add(tf.keras.layers.Conv2D(2, 5, strides=3, padding= 'valid', activation="relu"))
model.add(tf.keras.layers.Conv2D(4, 3, strides=1, padding= 'valid', activation="relu"))

model.add(tf.keras.layers.Flatten())

model.add(tf.keras.layers.Dense(2,activation="softmax"))

#Print model information:
model.summary()
