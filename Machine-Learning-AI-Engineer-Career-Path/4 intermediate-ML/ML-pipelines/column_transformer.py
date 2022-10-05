# Column Transformer
# Often times, you may not want to simply apply every function to all columns.
# If our columns are of different types, we may only want to apply certain parts
# of the pipeline to a subset of columns. This is what we saw in the two previous
# exercises. One set of transformations are applied to numeric columns and
# another set to the categorical ones. We can use ColumnTransformer as one way
# of combining these processes together.
#
# ColumnTransformer takes in a list of tuples of the form (name, transformer, columns).
# The transformer can be anything with a .fit and .transform method like we used
# previously (like SimpleImputer or StandardScaler), but can also itself be a
# pipeline, as we will use in the exercise.


import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import KFold, train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

columns = ["sex","length","diam","height","whole","shucked","viscera","shell","age"]
df = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data",names=columns)

y = df.age
X = df.drop(columns=['age'])
num_cols = X.select_dtypes(include=np.number).columns
cat_cols = X.select_dtypes(include=['object']).columns

#create some missing values
for i in range(1000):
    X.loc[np.random.choice(X.index),np.random.choice(X.columns)] = np.nan

x_train, x_test, y_train, y_test = train_test_split(X,y, random_state=0, test_size=0.25)

#Existing pipelines from previous two exercises
num_vals = Pipeline([("imputer",SimpleImputer(strategy='mean')), ("scale",StandardScaler())])
cat_vals = Pipeline([("imputer",SimpleImputer(strategy='most_frequent')), ("ohe", OneHotEncoder(sparse=False, drop='first'))])

#Create the column transformer with the categorical and numerical processes
preprocess = ColumnTransformer([("categorical", cat_vals, cat_cols), ("numerical", num_vals, num_cols)])

#fit the preprocess transformer
preprocess.fit(x_train)
transformed_data = preprocess.transform(x_test)
print(transformed_data.shape)
print(transformed_data)
