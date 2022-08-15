import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

coffee = pd.read_csv('starbucks_customers.csv')
ages = coffee['age']

## add code below
scaler = StandardScaler()
ages_reshaped = np.array(ages).reshape(-1,1)
ages_scaled = scaler.fit_transform(ages_reshaped)

print(np.mean(ages_scaled))
print(np.std(ages_scaled))
