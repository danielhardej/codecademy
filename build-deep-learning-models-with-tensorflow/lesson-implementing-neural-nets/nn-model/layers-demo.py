import tensorflow as tf
from tensorflow.keras import layers
layer = layers.Dense(3) #3 is the number we chose

print(layer.weights) #we get empty weight and bias arrays because tensorflow
                     #doesn't know what the shape is of the input to this layer

# 1338 samples, 11 features as in our dataset
input = tf.ones((5000, 21))
# a fully-connected layer with 3 neurons
layer = layers.Dense(10)
# calculate the outputs
output = layer(input)
# print the weights
print(layer.weights) 
