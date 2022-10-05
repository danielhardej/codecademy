# Data Cleaning (Categorical)
#
# For the categorical variables, let’s look at another common task – dealing
# with missing values and one-hot-encoding. We will convert an existing
# codebase to a pipeline, describing the two steps in detail.
#
# As in in the previous exercise, SimpleImputer will be used again to fill
# missing values in the pipeline, but this time, the strategy parameter will
# need to be updated to most_frequent. OneHotEncoder will be used as the
# second step in the pipeline. Note, that the default is that a sparse array
# will be returned from this transform, so we will use sparse='False' to
# return a full array.

import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import KFold, train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

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
df = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data", names=columns)

y = df.age
X=df.drop(columns=['age'])
num_cols = X.select_dtypes(include=np.number).columns
cat_cols = X.select_dtypes(include=['object']).columns

#create some missing values
for i in range(1000):
    X.loc[np.random.choice(X.index),np.random.choice(X.columns)] = np.nan

x_train, x_test, y_train, y_test = train_test_split(X,y, random_state=0, test_size=0.25)
x_train_cat = x_train[cat_cols]
x_test_cat = x_test[cat_cols]

#fill missing values with mode on numeric features only
x_train_fill_missing = x_train_cat.fillna(x_train_cat.mode().values[0][0])

#fit standard scaler on x_train_fill_missing
ohe = OneHotEncoder(sparse=False, drop='first').fit(x_train_fill_missing)

#scale data after filling in missing values
x_train_fill_missing_ohe = ohe.transform(x_train_fill_missing)

#Now want to do the same thing on the test set!
x_test_fill_missing = x_test[cat_cols].fillna(x_train_cat.mode().values[0][0])
x_test_fill_missing_ohe = ohe.transform(x_test_fill_missing)

#1. Rewrite using Pipelines!
pipe = Pipeline([("imputer",SimpleImputer(strategy='most_frequent')), ("ohe", OneHotEncoder(sparse=False, drop='first'))])
pipe.fit(x_train_cat)
x_test_transformed = pipe.transform(x_test_cat)

#2. Now apply the same thing on the test same as x_test_fill_missing_ohe
print('Verify pipeline transform test set is the same\nPrinting the sum of absolute differences (should be zero):')
print( get_sum_abs_diffs(x_test_transformed, x_test_fill_missing_ohe) )
