# Data Cleaning (Numeric)

# To introduce pipelines, let’s look at a common task – dealing with missing
# values and scaling numeric variables. We will convert an existing code base to
# a pipeline, describing these two steps in detail.

import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import KFold, train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score

# function to calculate the sum of absolute differences of two arrays
def get_sum_abs_diffs(arr1, arr2):
  diffs = []
  if len(arr1) == len(arr2):
    for i in range(len(arr1)):
      diffs.append(arr1[i] - arr2[i])
  else:
    pass
  return sum(diffs)

columns = ["sex","length","diam","height","whole","shucked","viscera","shell","age"]

df = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data",names=columns)

y = df.age
X=df.drop(columns=['age'])

# print(y.dtypes)
# print("---")
# print(X.dtypes)

num_cols = X.select_dtypes(include=np.number).columns
cat_cols = X.select_dtypes(include=['object']).columns

#create some missing values
for i in range(1000):
    X.loc[np.random.choice(X.index),np.random.choice(X.columns)] = np.nan

x_train, x_test, y_train, y_test = train_test_split(X,y, random_state=0, test_size=0.25)

x_train_num = x_train[num_cols]

#fill missing values with mean on numeric features only
x_train_fill_missing = x_train_num.fillna(x_train_num.mean())

#fit standard scaler on x_train_fill_missing
scale = StandardScaler().fit(x_train_fill_missing)

#scale data after filling in missing values
x_train_fill_missing_scale = scale.transform(x_train_fill_missing)

#Now want to do the same thing on the test set!
x_test_fill_missing = x_test[num_cols].fillna(x_train_num.mean())
x_test_fill_missing_scale = scale.transform(x_test_fill_missing)

x_test_num = x_test[num_cols]

#1. Rewrite using Pipelines!
pipe = Pipeline([("imputer",SimpleImputer(strategy='mean')), ("scale",StandardScaler())])

#2. Fit pipeline on the test and compare results
pipe.fit(x_train_num)
x_test_transformed = pipe.transform(x_test_num)
# print(x_test_transformed)

sum_abs_diff_mean = get_sum_abs_diffs(x_test_transformed, x_test_fill_missing_scale)
print(sum_abs_diff_mean)   # should be zero!

#3. Change imputer strategy to median and compare results
pipe_median = Pipeline([("imputer", SimpleImputer(strategy='median')), ("scale", StandardScaler())])
pipe_median.fit(x_train_num)
x_test_transformed_median = pipe_median.transform(x_test_num)

sum_abs_diff_median = get_sum_abs_diffs(x_test_transformed_median, x_test_fill_missing_scale)
print(sum_abs_diff_median)    # should be more than zero!
