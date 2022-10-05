# Adding a Model
#
# Now that we have all the preprocessing done and coded succinctly using
# ColumnTransformer and Pipeline, we can add a model. We will take the result at
# the end of the previous exercise, and now create a final pipeline with the
# ColumnTransformer as the first step, and a LinearRegression model as the
# second step.
#
# By adding a model to the final step, the last step no longer has a .transform
# method. This is the only step in a pipeline that can be a non-transformer. But
# now the final step also has a .predict method, which can be called on the
# entire pipeline.

import numpy as np
import pandas as pd

from sklearn import svm, datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

columns = ["sex","length","diam","height","whole","shucked","viscera","shell","age"]
df = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data",names=columns)

y = df.age
X=df.drop(columns=['age'])
num_cols = X.select_dtypes(include=np.number).columns
cat_cols = X.select_dtypes(include=['object']).columns
#create some missing values
for i in range(1000):
    X.loc[np.random.choice(X.index),np.random.choice(X.columns)] = np.nan

x_train, x_test, y_train, y_test = train_test_split(X,y, random_state=0, test_size=0.25)

cat_vals = Pipeline([("imputer",SimpleImputer(strategy='most_frequent')), ("ohe", OneHotEncoder(sparse=False, drop='first'))])
num_vals = Pipeline([("imputer",SimpleImputer(strategy='mean')), ("scale",StandardScaler())])

preprocess = ColumnTransformer(
    transformers=[
        ("cat_process", cat_vals, cat_cols),
        ("num_process", num_vals, num_cols)
    ]
)

#1. Create a pipeline with pregrocess and a linear regression model
pipe = Pipeline([("preprocess", preprocess), ("lrm", LinearRegression())])

#2. Fit the pipeline on the training data
pipe.fit(x_train, y_train)

#3. Predict the pipeline on the test data
y_pred = pipe.predict(x_test)
print(y_pred)
