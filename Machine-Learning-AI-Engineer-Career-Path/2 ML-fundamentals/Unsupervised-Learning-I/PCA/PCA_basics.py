# In the world of Machine Learning, any model that we implement will be more
# valuable when the features are engineered to suit the question we’re trying to
# answer. With many datasets, we can simply include all available features, which
# gives us the full picture about our observations. For example, it’s
# straightforward to see a correlation between height and weight for a patient
# dataset. Some datasets, however, have very large numbers of features. If our
# example patient dataset expanded to include 20 different features, how would we
# visualize and correlate this data? When it comes time to actually process the
# data and train the model, we often hit computational or complexity limits. How
# do we leverage correlations within the data to make fewer, better features
# without losing the information included in the dataset?
#
# Situations like this are a great use case for implementing Principal Component
# Analysis. PCA is a technique where we can reduce the number of features in a
# dataset without losing any of the information we have.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('pizza.csv')

print(df.columns)

df[['revenue','total_customers']].head()

#define function to calculate cv
cv = lambda x: np.std(x, ddof=1) / np.mean(x) * 100
covs = df.apply(cv)
sorted_covs = covs.sort_values(ascending = False)
print(sorted_covs)

# For a given dataset, we start by calculating a covariance matrix for all of our features.
#
# Afterwards, we perform matrix factorization, which will separate out the dataset and give us two results:
#   1) eigenvectors, also known as Principal Components, which define the direction, or "rotation", of our new data space
#   2) eigenvalues, which determine the magnitude of that new data space
