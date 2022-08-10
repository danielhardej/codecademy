# In addition to using bootstrapped samples of our dataset, we can continue to
# add variety to the ways our trees are created by randomly selecting the features
# that are used.

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data', names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'accep'])
df['accep'] = ~(df['accep']=='unacc') #1 is acceptable, 0 if not acceptable
X = pd.get_dummies(df.iloc[:,0:6], drop_first=True)
y = df['accep']
x_train, x_test, y_train, y_test = train_test_split(X,y, random_state=0, test_size=0.25)
dt = DecisionTreeClassifier(max_depth=5)
dt.fit(x_train, y_train)

# 1. Make new decision tree trained on random sample of 10 features and compare accuracies
dt2 = DecisionTreeClassifier()
# TODO: Create rand_features, which will contain random samples from the set of features (not entirely sure how to do this)
rand_features =
dt2.fit(x_train[rand_features], y_train)

print(f'Accuracy score of DT on test set (trained using full feature set): {dt.score(x_test, y_test).round(4)}')
print(f'Accuracy score of DT on test set (trained using radom feature sample): {dt2.score(x_test[rand_features], y_test).round(4)}')

# 2. Build decision trees on 10 different random samples and average the predictions
preds = []
random_state = 0
for i in range(10):
    ids = x_train.sample(x_train.shape[0], replace=True, random_state=random_state+i).index
    dt2.fit(x_train.loc[ids], y_train[ids])
    preds.append(dt2.predict(x_test))
ba_pred = np.array(preds).mean(0)

fa_pred = np.array(preds).mean(0)
fa_accuracy = accuracy_score(ba_pred>=0.5, y_test).round(4)
print(f'Accuracy score of aggregated 10 samples:{fa_accuracy}')
