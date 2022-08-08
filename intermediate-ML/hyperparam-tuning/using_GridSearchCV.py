from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

# Load the data set
cancer = load_breast_cancer()

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target)

# These are the hyperparameters that we will test.
# We'll try both 'l1' and 'l2' regularization.
# C is the inverse of regularization strength. Smaller C will result in stronger regularization.
parameters = {'penalty':['l1', 'l2'], 'C':[0.1, 1, 10, 100, 1000]}

# The logistic regression model
# The 'liblinear' solver is compatible with both 'l1' and 'l1' penalties.
# Setting max_iter to 1000 ensures that the solver will converge for this particular data set.
lr = LogisticRegression(solver='liblinear', max_iter=1000)

# Create a GridSearchCV model
# This will train the model 'lr' with each possible combination of hyperparameters in 'parameters'
clf = GridSearchCV(lr, parameters)

# Fit the GridSearchCV model
clf.fit(X_train, y_train)
