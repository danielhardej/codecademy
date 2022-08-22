# Credit card fraud is one of the leading causes of identify theft around the
# world. In 2018 alone, over $24 billion were stolen through fraudulent credit
# card transactions. Financial institutions employ a wide variety of different
# techniques to prevent fraud, one of the most common being Logistic Regression.
#
# In this project, you are a Data Scientist working for a credit card company.
# You have access to a dataset (based on a synthetic financial dataset), that
# represents a typical set of credit card transactions. Your task is to use
# Logistic Regression and create a predictive model to determine if a transaction
# is fraudulent or not.

# Dataset: https://www.kaggle.com/datasets/ealaxi/paysim1

import seaborn
import pandas as pd
import numpy as np
import codecademylib3
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

# Load the data
transactions = pd.read_csv('transactions.csv')
print(transactions.head())
print(transactions.info())

# Summary statistics on amount column
print(transactions['amount'].describe())

# Create isPayment field
transactions['isPayment'] = 0
transactions['isPayment'][transactions['type'].isin(['PAYMENT','DEBIT'])] = 1

# Create isMovement field
transactions['isMovement'] = 0
transactions['isMovement'][transactions['type'].isin(['CASH_OUT', 'TRANSFER'])] = 1

# Create accountDiff field
transactions['accountDiff'] = abs(transactions['oldbalanceOrg'] - transactions['oldbalanceDest'])

# Create features and label variables
features = transactions[['amount', 'isPayment', 'isMovement', 'accountDiff']]
labels = transactions[['isFraud']]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(features, labels,  test_size=0.3, random_state = 51)

# Normalize the features variables
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Fit the model to the training data
lrm = LogisticRegression()
lrm.fit(X_train, y_train)

# Score the model on the training data
print("Training score:")
print(lrm.score(X_train, y_train))

# Score the model on the test data
print("Test score:")
print(lrm.score(X_test, y_test))

# Score the model's predictions
y_pred = lrm.predict(X_test)
print("Acc score: ")
print(accuracy_score(y_test, y_pred))

print("Confusion matrix")
print(confusion_matrix(y_test, y_pred))

# Print the model coefficients
print("\nFeature coefficients")
for i in range(len(lrm.coef_[0])):
  print("  ", features.columns[i], ": ", lrm.coef_[0][i])

abs_coefs = [abs(ele) for ele in lrm.coef_[0]]
most = max(abs_coefs)
least = min(abs_coefs)
print("Most important:  ", features.columns[abs_coefs.index(most)])
print("Least important: ", features.columns[abs_coefs.index(least)])

# New transaction data
transaction1 = np.array([123456.78, 0.0, 1.0, 54670.1])
transaction2 = np.array([98765.43, 1.0, 0.0, 8524.75])
transaction3 = np.array([543678.31, 1.0, 0.0, 510025.5])

# Create a new transaction
your_transaction = np.array([54367.31, 1.0, 0.0, 51002.5])

# Combine new transactions into a single array
sample_transactions = np.stack((transaction1, transaction2, transaction3, your_transaction))
# print(sample_transactions)

# Normalize the new transactions
sample_transactions = scaler.transform(sample_transactions)

# Predict fraud on the new transactions
preds = lrm.predict(sample_transactions)
print("Predictions:")
print(preds)

# Show probabilities on the new transactions
pred_probas = lrm.predict_proba(sample_transactions)
print("Prediction probabilities: ")
print(pred_probas)
