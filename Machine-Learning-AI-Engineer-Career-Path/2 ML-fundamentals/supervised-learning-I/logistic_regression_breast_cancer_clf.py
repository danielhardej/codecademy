import codecademylib3_seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score

dataset = load_breast_cancer()
# print(dataset.keys())
# print(dataset.DESCR)
# print(dataset.feature_names)
# print(dataset.target_names)

df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
df['target'] = dataset.target
# print(df.head(20))
# print(df.info())

X = dataset.data
y = dataset.target
X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=0.2, random_state = 51)

lrm = LogisticRegression()
lrm.fit(X_train, y_train)

y_pred = lrm.predict(X_test)

# Print out the confusion matrix
print('Confusion matrix: ')
print(confusion_matrix(y_test, y_pred))

# Print accuracy here:
print("Accuracy score:")
print(accuracy_score(y_test, y_pred))

# Print F1 score here:
print("F1 score: ")
print(f1_score(y_test, y_pred))
