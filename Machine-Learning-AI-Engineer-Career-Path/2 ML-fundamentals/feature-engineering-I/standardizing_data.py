# Standardization (also known as Z-Score normalization) is when we center our data,
# then divide it by the standard deviation. Once we do that, our entire data set
# will have a mean of zero and a standard deviation of one. Which is allowing all
# of our features to be on the same scale.

import pandas as pd
import numpy as np

coffee = pd.read_csv('starbucks_customers.csv')
ages = coffee['age']

## add code below
## set up your variables
mean_age = np.mean(ages)
std_dev_age = np.std(ages)

## standardize ages
ages_standardized = (ages - mean_age) / std_dev_age

## print the results
print(np.mean(ages_standardized))
print(np.std(ages_standardized))
