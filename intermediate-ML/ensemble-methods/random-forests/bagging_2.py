import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, BaggingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data', names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'accep'])
df['accep'] = ~(df['accep']=='unacc') #1 is acceptable, 0 if not acceptable
X = pd.get_dummies(df.iloc[:,0:6], drop_first=True)
y = df['accep']
x_train, x_test, y_train, y_test = train_test_split(X,y, random_state=0, test_size=0.25)

# 1. Bagging classifier with 10 Decision Tree base estimators
bag_dt = BaggingClassifier(DecisionTreeClassifier(max_depth=5), n_estimators=10)
bag_dt.fit(x_train, y_train)
print('Accuracy score of Bagged Classifier, 10 estimators:')
print(bag_dt.score(x_test, y_test).round(4))

# 2.Set `max_features` to 10.
bag_dt_10 = BaggingClassifier(DecisionTreeClassifier(max_depth=5), n_estimators=10, max_features=10)
bag_dt_10.fit(x_train, y_train)
print('Accuracy score of Bagged Classifier, 10 estimators, 10 max features:')
print(bag_dt_10.score(x_test, y_test).round(4))

# 3. Change base estimator to Logistic Regression
bag_lr = BaggingClassifier(LogisticRegression(), n_estimators=10)
bag_lr.fit(x_train, y_train)
print('Accuracy score of Logistic Regression, 10 estimators:')
print(bag_lr.score(x_test, y_test).round(4))
