#### What can we use if we want to generate more image data without collecting any new images?

We can use data augmentation.

#### Complete the command below to create a convolutional neural network layer with 5 filters, each with size 3x3, that uses a ReLU activation function.

 model.add(tf.keras.layers.Conv2D(5, 3,activation="relu"))


#### Fill in the code below to create a Dense layer with 16 hidden units and uses a rectified linear unit.

from tensorflow.keras.layers import  Dense
model.add(Dense(16, activation='relu'))


#### Why should we use sklearn.preprocessing.LabelEncoder instead of pandas.get_dummies() when performing one-hot encoding on labels rather than features?

get_dummies() creates a separate column for each category, and you cannot predict for multiple columns.


#### Which of the following is NOT a reason to use Conv2D layers instead of Dense layers for image data?

Convolutional layers are less computationally expensive than dense layers.

#### In the following code block, what does padding="valid" do?

model.add(tf.keras.layers.Conv2D(5, 5, strides=2, padding="valid", activation="relu"))

The padding hyperparameter defines what we do once our filter gets to the end of a row/column. With the value "valid", the filter just stops when our kernel moves off the image.

#### When we perform cross-entropy, the goal is to get our score as close as possible to which of the following values?

- [ ] 100
- [ ] 1
- [ ] There is no specific value we are aiming to get close to.
- [x] 0


#### What does a Flatten layer do?

- [ ] It reduces the dimensionality of intermediate convolutional outputs.
- [ ] Nothing, there is no Flatten() layer.
- [x] It flattens the output of convolutional layers before passing them into a Dense layer.


#### If we are working with tabular data, what type of hidden layers should we use for our classification model?

- [ ] Tabular Layers
- [ ] Convolution Layers
- [x] Dense Layers
- [ ] We can’t use any hidden layers.

#### You want to compile your classification learning model with a few specifications:
- You want to use sparse categorical cross-entropy as your loss function.
- You want to use an Adam optimizer.
- You want to use performance accuracy as your performance metric.
##### Fill in the code below so that it accurately reflects these specifications.

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])



#### Lower-level filters tend to pick up simpler patterns, while high high-level filters tend to identify more abstract information, such as “is this a dog or a cat?”.

- [ ] False
- [x] True



#### Complete the code below to load and batch a set of color images using an image generator called training_data_generator. We would like them to have a height and width of 256 by 256 pixels and be put in batches of size 64.

training_iterator = training_data_generator.flow_from_directory(DIRECTORY, class_mode=CLASS_MODE, color_mode='rgb', target_size=(256, 256), batch_size=64)
