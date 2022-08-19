# Honey Production

# Now that you have learned how linear regression works, let’s try it on an
# example of real-world data.

# As you may have already heard, the honeybees are in a precarious state right
# now. You may have seen articles about the decline of the honeybee population for 
# various reasons. You want to investigate this decline and how the trends of the
# past predict the future for the honeybees.

import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("https://content.codecademy.com/programs/data-science-path/linear_regression/honeyproduction.csv")

### Check out the Data
print(df.head())

prod_per_year = df.groupby('year').totalprod.mean().reset_index()

X = prod_per_year['year']
X = X.values.reshape(-1, 1)

y = prod_per_year['totalprod']

plt.scatter(X, y)

### Create and Fit a Linear Regression Model
lrm = linear_model.LinearRegression()
lrm.fit(X, y)

print("Slope: {}".format(lrm.coef_))
print("Intercept: {}".format(lrm.intercept_))

y_predict = lrm.predict(X)
plt.plot(X, y_predict)
plt.show()

### Predict the Honey Decline
X_future = np.array(range(2013, 2051))
X_future = X_future.reshape(-1, 1)
future_predict = lrm.predict(X_future)

X_final = np.array([2050])
X_final = X_final.reshape(-1,1)
y_pred_2050 = lrm.predict(X_final)

print("Estimated production in 2050: {}".format(y_pred_2050))

plt.plot(X_future, future_predict)
plt.show()
