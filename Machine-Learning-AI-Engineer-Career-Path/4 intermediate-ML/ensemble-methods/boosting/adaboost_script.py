import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Load dataset to a pandas DataFrame
path_to_data = 'https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data'
column_names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'accep']
df = pd.read_csv(path_to_data, names=column_names)

target_column = 'accep'
raw_feature_columns = [col for col in column_names if col != target_column]

# Create dummy variables from the feature columns
X = pd.get_dummies(df[raw_feature_columns], drop_first=True)

# Convert target column to binary variable; 0 if 'unacc', 1 otherwise
df[target_column] = np.where(df[target_column] == 'unacc', 0, 1)
y = df[target_column]

# Split the full dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=123, test_size=0.3)

# 1. Create a decision stump base model using the Decision Tree Classifier and print its parameters
decision_stump = DecisionTreeClassifier()
#print(decision_stump.get_params())

# 2. Create an Adaptive Boost Classifier and print its parameters
ada_classifier = AdaBoostClassifier(base_estimator=decision_stump, n_estimators=5)
#print(ada_classifier.get_params())

# 3. Fit the Adaptive Boost Classifier to the training data and get the list of predictions
ada_classifier.fit(X_train, y_train)
y_pred = ada_classifier.predict(X_test)
#y_pred = cross_val_predict(ada_classifier, X, y, cv=2)

# 4. Calculate the accuracy, precision, recall, and f1-score on the testing data
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# 5. Remove the comments from the following code block to print the confusion matrix
print("Accuracy score: ", accuracy)
print("Precision score: ", precision)
print("Recall score: ", recall)
print("F1 score: ", f1)
print("Confusion matrix: ")
print(confusion_matrix(y_test, y_pred))
