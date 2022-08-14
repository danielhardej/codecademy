import pandas as pd
import numpy as np
import codecademylib3
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data', names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'accep'])

## 1. Print number of rows and distribution of safety ratings
nrows = len(df.index)
print(nrows)
print(f'Distribution of safety ratings in {nrows} rows of data:')
print(df.safety.value_counts(normalize=True))

## 2. Create bootstrapped sample
boot_sample = df.sample(nrows, replace=True)
print(f'Distribution of safety ratings in bootstrapped sample data:')
print(boot_sample.safety.value_counts(normalize=True))

## 3. Create 1000 bootstrapped samples
low_perc = []
for i in range(1000):
  boot_sample = df.sample(nrows, replace=True)
  low_perc.append(boot_sample.safety.value_counts(normalize=True)['low'])

## 4. Plot a histogram of the low percentage values
mean_lp = np.mean(low_perc)
print(mean_lp)
plt.hist(low_perc, bins=20);
plt.xlabel('Low Percentage')
plt.show()
