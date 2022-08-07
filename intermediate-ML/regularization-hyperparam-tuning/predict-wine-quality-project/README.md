# Codecademy Intermediate Machine Learning
## Predict Wine Quality with Regularization Project

The data we’re working with is from the Wine Quality Dataset in the UCI Machine Learning Repository. We’re looking at the red wine data in particular and while the original dataset has a 1-10 rating for each wine, we’ve made it a classification problem with a wine quality of good (>5 rating) or bad (<=5 rating). The goals of this project are to:

 - implement different logistic regression classifiers
 - find the best ridge-regularized classifier using hyperparameter tuning
 - implement a tuned lasso-regularized feature selection method

What we’re working with:

 - 11 input variables (based on physicochemical tests): ‘fixed acidity’, ‘volatile acidity’, ‘citric acid’, ‘residual sugar’,’chlorides’, ‘free sulfur dioxide’, ‘total sulfur dioxide’,  ‘density’, ‘pH’, ‘sulphates’ and ‘alcohol’.
 - An output variable, ‘quality’ (0 for bad and 1 for good)

See the file 'wine_quality.csv' for the data set we use and 'script.py' for the code. We use the numpy, pandas, and sklearn libraries to test out L1 and L2 regularization and test out different hyperparameters.
