# With grid search, we made a list of different hyperparameter values and tested
# each combination of them. As an alternative, we could select hyperparameters
# randomly. Here’s how we might test different
# possible settings for two different hyperparameters.

import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import uniform

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
