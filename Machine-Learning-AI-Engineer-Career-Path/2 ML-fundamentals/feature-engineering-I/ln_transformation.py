# Logarithms are an essential tool in statistical analysis and machine learning
# preparation. This transformation works well for right-skewed data and data with
# large outliers. After we log transform our data, one large benefit is that it
# will allow the data to be closer to a “normal” distribution. It also changes the
# scale so our data points will drastically reduce the range of their values.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn

## add code below
## read in csv file
cars = pd.read_csv('cars.csv')

## set you price variable
prices = cars['sellingprice']

# ## plot a histogram of prices
# plt.hist(prices, bins = 150)
# plt.show()

## log transform prices
log_prices = np.log(prices)

## plot a histogram of log_prices
plt.hist(log_prices, bins = 150)
plt.show()
