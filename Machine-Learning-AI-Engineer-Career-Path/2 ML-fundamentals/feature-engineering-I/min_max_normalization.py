# we find the minimum and maximum data point in our entire data set and set each
# of those to 0 and 1, respectively. Then the rest of the data points will
# transform to a number between 0 and 1, depending on its distance between the
# minimum and maximum number. We find that transformed number by taking the data
# point subtracting it from the minimum point, then dividing by the value of our
# maximum minus minimum.
#
# One thing to note about min-max normalization is that this transformation does
# not work well with data that has extreme outliers. You will want to perform a
# min-max normalization if the range between your min and max point is not too drastic.

import pandas as pd
import numpy as np

coffee = pd.read_csv('starbucks_customers.csv')

## write you code below
spent = coffee['spent']
max_spent = np.max(spent)
min_spent = np.min(spent)

spent_range = max_spent - min_spent
print(spent_range)

spent_normalized = (spent - min_spent) / spent_range

print(spent_normalized)
