from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import uniform
from skopt import BayesSearchCV
from skopt.space import Categorical, Real
import pandas as pd

# Load the data set
cancer = load_breast_cancer()

# Split the data into training and testing sets
X = cancer.data
y = cancer.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

# These are the hyperparameters that we will test.
# We'll try both 'l1' and 'l2' regularization.
# C is the inverse of regularization strength. Smaller C will result in stronger regularization.
distributions = {'penalty':['l1', 'l2'], 'C':uniform(loc=0, scale=100)}

# The logistic regression model
lr = LogisticRegression(solver = 'liblinear', max_iter = 1000)

# Create a RandomizedSearchCV model
clf = RandomizedSearchCV(lr, distributions, n_iter=8)

# Fit the RandomizedSearchCV model
clf.fit(X_train, y_train)

# Show which hyperparameters performed the best
print(clf.best_estimator_)

# Print the the parameters and mean test score
print(clf.cv_results_['params'])
print(clf.cv_results_['mean_test_score'])

# Create and print Pandas DataFrame
df = pd.concat([pd.DataFrame(clf.cv_results_['params']), pd.DataFrame(clf.cv_results_['mean_test_score'], columns=['Accuracy'])] ,axis=1)

print(df.sort_values('Accuracy', ascending = False))

# Assess the model's accuracy on the testing data
acc = clf.score(X_test, y_test)
print(acc)
