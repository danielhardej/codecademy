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

columns = ["sex","length","diam","height","whole","shucked","viscera","shell","age"]

df = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data",names=columns)

y = df.age
X=df.drop(columns=['age'])

print(y.dtypes)
print("---")
print(X.dtypes)

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

#1. Rewrite using Pipelines!
pipe = Pipeline([("imputer", SimpleImputer(missing_values=np.nan)), ("scale", StandardScaler(with_mean=False))])

#2. Fit pipeline on the test and compare results
pipe.fit(x_train, y_train)
y_pred_mean = pipe.predict(x_test)
mean_accuracy = accuracy_score(y_test, y_pred_mean)

#3. Change imputer strategy to median and compare results
pipe_2 = Pipeline([("imputer", SimpleImputer(missing_values=np.nan, strategy='median')), ("scale", StandardScaler(with_mean=False))])

pipe_2.fit(x_train, y_train)
y_pred_med = pipe_2.predict(x_test)
med_accuracy = accuracy_score(y_test, y_pred_med)

print("Pipeline accuracy with mean impute strategy: {0}".format(mean_accuracy))
print("Pipeline accuracy with median impute strategy: {0}".format(med_accuracy))
