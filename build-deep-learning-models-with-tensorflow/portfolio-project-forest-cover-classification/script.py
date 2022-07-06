# In this project, you will use deep learning to predict forest cover type (the most
# common kind of tree cover) based only on cartographic variables. The actual forest
# cover type for a given 30 x 30 meter cell was determined from US Forest Service (USFS)
# Region 2 Resource Information System data. The covertypes are the following:
#
#     Spruce/Fir
#     Lodgepole Pine
#     Ponderosa Pine
#     Cottonwood/Willow
#     Aspen
#     Douglas-fir
#     Krummholz
#
# Independent variables were then derived from data obtained from the US Geological Survey
# and USFS. The data is raw and has not been scaled or preprocessed for you. It contains
# binary columns of data for qualitative independent variables such as wilderness areas
# and soil type.
#
# This study area includes four wilderness areas located in the Roosevelt National Forest
# of northern Colorado. These areas represent forests with minimal human-caused disturbances,
# so existing forest cover types are mainly a result of ecological processes rather
# than forest management practices.
#
# Project Objectives:
#     Develop one or more classifiers for this multi-class classification problem.
#     Use TensorFlow with Keras to build your classifier(s).
#     Use your knowledge of hyperparameter tuning to improve the performance of your model(s).
#     Test and analyze performance.
#     Create clean and modular code.

import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from collections import Counter
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report
from sklearn.metrics import classification_report, confusion_matrix

from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping    # TODO
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.metrics import CategoricalAccuracy, AUC

tf.random.set_seed(42) # for the reproducibility of results

# Turn off GPU usage for tf
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
os.environ["TF_CPP_MIN_LOG_LEVEL"] = '2'

### Define Hyperparameters ###
NUM_LAYERS = 4
NUM_NEURONS = 128
NUM_EPOCHS = 100
BATCH_SIZE = 16
LEARN_RATE=0.01
VAL_SPLT=0.2


def process_data(data):
    labels = dataset.iloc[:,-1]
    features = dataset.iloc[:,0:-1]
    features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.33, random_state=42, stratify=y)

    stan_scaler = StandardScaler()
    features_train_normalized = stan_scaler.fit_transform(features_train)
    features_test_normalized = stan_scaler.transform(features_test)

    ct = ColumnTransformer([('numeric',
                            StandardScaler(),
                            ["Elevation", "Aspect","Slope","Horizontal_Distance_To_Hydrology","Vertical_Distance_To_Hydrology",
                                "Horizontal_Distance_To_Roadways","Hillshade_9am","Hillshade_Noon","Hillshade_3pm","Horizontal_Distance_To_Fire_Points"],
                            remainder='passthrough')])

    features_train_scale = ct.fit_transform(features_train)
    features_test_scale = ct.transform(features_test)

    return features_train_scale, features_test_scale, labels_train, labels_test


def build_model(n_layers, n_neurons):
    model = Sequential()
    # create input layer
    model.add(InputLayer(input_shape=(features_train_scale.shape[1],)))
    # create hidden layers
    layer_count = 0
    for i in range(n_layers):
        if n_neurons>8:
            model.add(Dense(n_neurons, activation='relu'))
        else:
            pass
        layer_count +=1
        n_neurons = n_neurons/2
    # create output layer
    model.add(Dense(8, activation='softmax'))
    return model


def train_model(features_train_scaled, labels_train):
    opt = Adam(learning_rate=LEARN_RATE)
    my_model.compile(loss='mse', metrics='mae', optimizer=opt)
    history = my_model.fit(features_train_scaled, labels_train, epochs=N_EPOCHS, batch_size=BATCH_SIZE, verbose=1, validation_split=VAL_SPLT)
    return history

def plot_results():

    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'val'], loc='upper left')
    plt.show()

    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'val'], loc='upper right')
    plt.show()

def evaluate_model():

    res_mse, res_mae = my_model.evaluate(features_test_scaled, labels_test, verbose=0)
    predicted_values = my_model.predict(features_test_scaled)
    r2score = r2_score(labels_test, predicted_values)

    loss, acc = model.evaluate(features_test_scale, labels_test, verbose=0)

    print("Model summary: ")
    print(model.summary())
    print()
    print("Loss: ", loss)
    print("Accuracy: ", acc)
    print()
    print("Summary: ")
    print("Number of layers: " + str(layer_count))
    print("Number of neurons: " + str(N_NEURONS))
    print("Batch size: "  + str(BATCH_SIZE))
    print("Number of epochs: " + str(N_EPOCHS))
    print("Learning rate: " + str(L_RATE))
    print("Validation split: " + str(VAL_SPLT))
    print("R2 score: " + str(r2score))
    print("Final loss (RMSE): "  +  str(res_mse))
    print("MAE: " + str(res_mae))
    # print(h1.history.keys())
    print(my_model.summary())

def generate_classification_report():
    prediction = np.argmax(model.predict(features_test_scale), axis=1)
    labels_test = np.argmax(labels_test, axis=1)
    class_names = ['Spruce/Fir', 'Lodgepole Pine', 'Ponderosa Pine', 'Cottonwood/Willow', 'Aspen', 'Douglas-fir', 'Krummholz']
    print()
    print(classification_report(labels_test, prediction, target_names=class_names))


def main():
    dataframe = pd.read_csv("cover_data.csv")
    features_train_scale, features_test_scale, labels_train, labels_test = process_data(dataframe)
    train_model()
    plot_results()
    evaluate_model()
    generate_classification_report()


if __name__ == '__main__':
    main()
