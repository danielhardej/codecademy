import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, RandomForestRegressor
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score, mean_absolute_error


df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data', names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'accep'])
df['accep'] = ~(df['accep']=='unacc') #1 is acceptable, 0 if not acceptable
X = pd.get_dummies(df.iloc[:,0:6], drop_first=True)
y = df['accep']
x_train, x_test, y_train, y_test = train_test_split(X,y, random_state=0, test_size=0.25)

# 1. Create a Random Forest Classifier and print its parameters
rf = RandomForestClassifier()
print("RFC parameters:")
for param in rf.get_params().items():
  print(param)

# 2. Fit the Random Forest Classifier to training data and calculate accuracy score on the test data
rf.fit(x_train, y_train)
y_pred = rf.predict(x_test)
print("\nRFC accuracy score: ", accuracy_score(y_test, y_pred))
print("RFC F1 score: ", f1_score(y_test, y_pred))
#print("RFC MSE score: ", mean_absolute_error(y_test, y_pred))

# 3. Calculate Precision and Recall scores and the Confusion Matrix
print("RFC precision score: ", precision_score(y_test, y_pred))
print("RFC recall score: ", recall_score(y_test, y_pred))
print("Confusion matrix: ")
print(confusion_matrix(y_test, y_pred))
