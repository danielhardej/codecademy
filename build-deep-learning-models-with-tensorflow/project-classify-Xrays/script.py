import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.metrics import CategoricalAccuracy, AUC

import matplotlib.pyplot as plt
import app
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix

### Set hyperparams ###
NUM_EPOCHS = 20
BATCH_SIZE = 8
LEARN_RATE = 0.01

CLASS_MODE = "categorical"
COLOR_MODE = "grayscale"
TARGET_SIZE = (256,256)
BATCH_SIZE = 32
TRAIN_DATA_DIRECTORY = "augmented-data/train"
TEST_DATA_DIRECTORY = "augmented-data/test"

### Loading the data ###
train_image_data_generator = ImageDataGenerator(rescale=1.0/255,
                                            zoom_range=0.2,
                                            rotation_range=15,
                                            width_shift_range=0.05,
                                            height_shift_range=0.05)

training_iterator = train_image_data_generator.flow_from_directory(TRAIN_DATA_DIRECTORY,
                                                                class_mode=CLASS_MODE,
                                                                color_mode=COLOR_MODE,
                                                                target_size=TARGET_SIZE,
                                                                batch_size=BATCH_SIZE)


test_image_data_generator = ImageDataGenerator(rescale=1.0/255)

test_iterator = test_image_data_generator.flow_from_directory(TEST_DATA_DIRECTORY,
                                                        class_mode=CLASS_MODE,
                                                        color_mode=COLOR_MODE,
                                                        target_size=TARGET_SIZE,
                                                        batch_size=BATCH_SIZE)
# print()
# print(test_iterator.__dict__)
# print(training_iterator.__dict__)

### Design the model ###
model = tf.keras.Sequential()
model.add(tf.keras.Input(shape = (256,256,1)))

# add convolutional layers
model.add(tf.keras.layers.Conv2D(8, 3, strides=2, activation="relu"))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

model.add(tf.keras.layers.Conv2D(8, 3, strides=2, activation="relu"))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

model.add(tf.keras.layers.Dense(16, activation = "relu"))

# add output layer that outputs 3 features/classes: Covid, Normal, or Viral Pneumonia
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(3, activation="softmax"))

model.compile(
            optimizer = tf.keras.optimizers.Adam(learning_rate=LEARN_RATE),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=[tf.keras.metrics.CategoricalAccuracy(), tf.keras.metrics.AUC()]
            )

model.summary()

### Train and evaluate the model ###
history = model.fit(
       training_iterator,
       steps_per_epoch = (training_iterator.samples)/BATCH_SIZE,
       epochs = NUM_EPOCHS,
       validation_data = test_iterator,
       validation_steps = (test_iterator.samples)/BATCH_SIZE
)


### Plot the cross-entropy loss for both the train and validation data over each epoch ###
fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax1.plot(history.history['categorical_accuracy'])
ax1.plot(history.history['val_categorical_accuracy'])
ax1.set_title('model accuracy')
ax1.set_xlabel('epoch')
ax1.set_ylabel('accuracy')
ax1.legend(['train', 'validation'], loc='upper left')

ax2 = fig.add_subplot(2, 1, 2)
ax2.plot(history.history['auc'])
ax2.plot(history.history['val_auc'])
ax2.set_title('model auc')
ax2.set_xlabel('epoch')
ax2.set_ylabel('auc')
ax2.legend(['train', 'validation'], loc='upper left')
# Do Matplotlib extension below
fig.tight_layout()
fig.savefig('static/images/my_plots.png')


###  implement classification report and confusion matrix ###
model_predictions = model.predict(test_iterator, steps=(test_iterator.samples)/BATCH_SIZE)

predicted_classes = np.argmax(model_predictions, axis=1)
true_classes = test_iterator.classes
class_labels = list(test_iterator.class_indices.keys())

print("Classification Report:")
print(classification_report(true_classes, predicted_classes, target_names=class_labels))

print("Confusion Matrix:")
print(confusion_matrix(true_classes,predicted_classes, labels = [0,1,2]))
