# Binning data is the process of taking numerical or categorical data and breaking
# it up into groups. We could decide to bin our data to help capture patterns in
# noisy data. There isn’t a clean and fast rule about how to bin your data, but
# like so many things in machine learning, you need to be aware of the trade-offs.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn

coffee = pd.read_csv('starbucks_customers.csv')
ages = coffee['age']

print(np.min(ages))
print(np.max(ages))

age_bins = [12, 20, 30, 40, 71]

coffee['binned_ages'] = pd.cut(ages, age_bins, right = False)

print(coffee['binned_ages'].head(10))

coffee['binned_ages'].value_counts().plot(kind='bar')
plt.show()
