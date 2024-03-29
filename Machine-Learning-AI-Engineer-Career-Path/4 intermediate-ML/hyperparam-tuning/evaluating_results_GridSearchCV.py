import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

# Load the data set
cancer = load_breast_cancer()

# Split the data into training and testing sets
X = cancer.data
y = cancer.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

# The hyperparameters that we will test.
parameters = {'penalty': ['l1', 'l2'], 'C': [0.1, 1, 10, 100]}

# The logistic regression model
# The 'liblinear' solver is compatible with both 'l1' and 'l2' penalties.
# Setting max_iter to 1000 ensures that the solver will converge for this particular data set.
lr = LogisticRegression(solver = 'liblinear', max_iter = 1000)

# Create a GridSearchCV model
clf = GridSearchCV(lr, parameters)

# Fit the GridSearchCV model
clf.fit(cancer.data, cancer.target)

# Print the hyperparameters that performed the best.
print(clf.best_estimator_)

# Print every combination of hyperparameters that you tested.
print(clf.cv_results_['params'])

# Print the score of the model with each combination of hyperparameters.
print(clf.cv_results_['mean_test_score'])

# This Pandas DataFrame tabulates hyperparameter values and the associated scores.
df = pd.concat([pd.DataFrame(clf.cv_results_['params']), pd.DataFrame(clf.cv_results_['mean_test_score'], columns=['Accuracy'])], axis=1)

# This table displays the information more clearly.
cv_table = df.pivot(index = 'C', columns = 'penalty')
print(cv_table)

# Compute and print the accuracy of the model on test data
acc = clf.score(X_test, y_test)
print(acc)
