import numpy as np
import pandas as pd

from sklearn import svm, datasets
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn import metrics

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

cat_vals = Pipeline([("imputer",SimpleImputer(strategy='most_frequent')), ("ohe",OneHotEncoder(sparse=False, drop='first'))])
num_vals = Pipeline([("imputer",SimpleImputer(strategy='mean')), ("scale",StandardScaler())])

preprocess = ColumnTransformer(
    transformers=[
        ("cat_process", cat_vals, cat_cols),
        ("num_process", num_vals, num_cols)
    ]
)
#Create a pipeline with preprocess and a linear regression model
pipeline = Pipeline([("preprocess",preprocess),
                     ("regr",LinearRegression())])

#Very simple parameter grid, with and without the intercept
param_grid = {
    "regr": [LinearRegression()],
    "regr__fit_intercept": [True,False]
}

# 1. Update the search_space dictionary to include values for alpha in lasso and ridge regression models. Use np.logspace(-4,2,10).
param_grid['regr__alpha'] = np.logspace(-4,2,10)
param_grid['regr'] = [Lasso(), Ridge()]

# 2.  Fit the GridSearchCV on the training data and print the best estimator and score from the search.
gscv = GridSearchCV(pipeline, param_grid, scoring='neg_mean_squared_error', cv=5)
gscv.fit(x_train, y_train)
# print(gscv.best_params_)
print(gscv.best_score_)

#3. Save the best estimator and print it
best_model = gscv.best_estimator_
print(best_model)

#4. Access the hyperparameters of the categorical preprocessing step
print(preprocess.get_params().keys())
