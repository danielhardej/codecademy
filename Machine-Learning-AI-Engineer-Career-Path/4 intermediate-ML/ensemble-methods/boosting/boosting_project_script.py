# ==============================================================================
# In this project, we will be using a dataset containing census information from
# UCI’s Machine Learning Repository.
#
# By using this census data with boosting algorithms, we will try to predict
# whether or not a person makes more than $50,000.
#
# The classifiers we use are the sklearn DecisionTreeClassifier,
# AdaBoostClassifier, and GradientBoostingClassifier. We also use GridSearchCV for
# tuning hyperparameters in order to find the best values for n_estimators and
# learning_rate.
#
# The original data set is available at the UCI Machine Learning Repository:
#     https://archive.ics.uci.edu/ml/datasets/census+income
# ==============================================================================

import pandas as pd
import numpy as np
import codecademylib3

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

path_to_data = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"

col_names = [
    'age', 'workclass', 'fnlwgt','education', 'education-num', 'marital-status',
    'occupation', 'relationship', 'race', 'sex', 'capital-gain','capital-loss',
    'hours-per-week','native-country', 'income'
]

df = pd.read_csv(path_to_data, header=None, names = col_names)

#Clean columns by stripping extra whitespace for columns of type "object"
for c in df.select_dtypes(include=['object']).columns:
    df[c] = df[c].str.strip()

target_column = "income"
raw_feature_cols = [
    'age',
    'education-num',
    'workclass',
    'hours-per-week',
    'sex',
    'race'
]

print(df[target_column].value_counts(normalize=True))
print(df[raw_feature_cols].dtypes)

X = pd.get_dummies(df[raw_feature_cols], drop_first=True)
# print(X.head(n=5))
y = np.where(df.income=='<=50K', 0, 1)
x_train, x_test, y_train, y_test = train_test_split(X,y, random_state=0, test_size=0.30)

decision_stump = DecisionTreeClassifier(max_depth=1)
ada_classifier = AdaBoostClassifier(base_estimator=decision_stump)
grad_classifier = GradientBoostingClassifier()

ada_classifier.fit(x_train, y_train)
grad_classifier.fit(x_train, y_train)

y_pred_ada = ada_classifier.predict(x_test)
y_pred_grad = grad_classifier.predict(x_test)

ada_acc = accuracy_score(y_test, y_pred_ada)
ada_f1 = f1_score(y_test, y_pred_ada)
grad_acc = accuracy_score(y_test, y_pred_grad)
grad_f1 = f1_score(y_test, y_pred_grad)

print("Results with default hyper-params...")
print("AdaBoost Classifier accuracy: {0}  F1: {1}".format(ada_acc, ada_f1))
print("GradBoost Classifier accuracy: {0}  F1: {1}".format(grad_acc, grad_f1))

# The hyperparameters that we will test for AdaBoost
# ada_params = {'n_estimators': list(range(10,101))}
# ada_gs_clf = GridSearchCV(ada_classifier, ada_params)
# ada_gs_clf.fit(x_train, y_train)
# print(ada_gs_clf.best_estimator_)

abc = AdaBoostClassifier()
parameters = {'n_estimators':[10,50,100,150,200,250,300]}
clf = GridSearchCV(abc, parameters,verbose=1,scoring='f1' ,n_jobs=-1)
clf.fit(x_train, y_train)
# Print the hyperparameters that performed the best.
print("Best AdaBoost parameters: ")
print(clf.best_params_)

# for n in range(10,101):
#   ada_classifier = AdaBoostClassifier(base_estimator=decision_stump, n_estimators=n)
#   ada_classifier.fit(x_train, y_train)
#   y_pred_ada = ada_classifier.predict(x_test)
#   ada_acc = accuracy_score(y_test, y_pred_ada)
#   ada_f1 = f1_score(y_test, y_pred_ada)

# print("AdaBoost Classifier best n_estimators {0} best accuracy: {1}  best F1: {2}".format(best_n, ada_best_acc, ada_f1))

gbc = GradientBoostingClassifier()
gbc_params = {'learning_rate':[0.01,0.1]}
gbc_clf = GridSearchCV(gbc, gbc_params,verbose=1,scoring='f1',n_jobs=-1)
gbc_clf.fit(x_train,y_train)
print("Best GradBoost params: ")
print(gbc_clf.best_params_)
